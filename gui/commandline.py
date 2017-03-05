#! /usr/bin/env python
# -*- coding:utf-8 -*-



import ruleset


def parseArgs(argv, action=False):
    """
    Parsing argv for arguments
    """
    import getopt
    opts, args = getopt.getopt(argv, "hdl:c:r:f:", ["help", "debug", "logfile=", "count", "roll=", "file=", "logformat="])

    import os
    import logging
    logconfig = {"format": "%(asctime)s: [%(levelname)s]:\t%(message)s"}
    debug = os.environ.get('DEBUG', False)
    print(debug)
    if debug:
        logconfig["level"] = logging.DEBUG
        logconfig["filename"] = "debug.log"

    
    options = dict()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            raise getopt.GetoptError("")
        elif opt in ("-d", "--debug"):
            logconfig["level"] = logging.DEBUG
        elif opt in ("-l", "--logfile"):
            logconfig["filename"] = arg
        elif opt in ("--logformat"):
            logconfig["format"] = arg
        elif opt in ("-c", "--count"):
            options["count"] = int(arg)
        elif opt in ("-r", "--roll"):
            methods = {
                "standard": ruleset.roll.STANDARD,
                "classic": ruleset.roll.CLASSIC,
                "heroic": ruleset.roll.HEROIC,
            }
            options["rollMethod"] = methods[arg]
        elif opt in ("-f", "--file"):
            options["filename"] = arg
    if len(args) > 0:
        if action:
            options["action"] = args.pop(0)
        options["args"] = args

    logging.basicConfig(**logconfig)
    return options
