#! /usr/bin/env python
# -*- coding:utf-8 -*-


import pathfinder.ruleset


def logOptions(options):
    logconfig = {"format": "%(asctime)s: [%(levelname)s]:\t%(message)s"}
    filename = [
        options.get("-l", None),
        options.get("--logfile", None),
    ]
    logformat = options.get("--logformat", None)
    if filename is not None:
        logconfig["filename"] = filename
    if logformat is not None:
        logconfig["format"] = logformat


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
    if debug:
        logconfig["level"] = logging.DEBUG
        logconfig["filename"] = "debug.log"

    options = dict()
    o = {opt: arg for opt, arg in opts}
    logOptions(options)

    print("OPTS: ", opts, o)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            raise getopt.GetoptError("")
        elif opt in ("-d", "--debug"):
            logconfig["level"] = logging.DEBUG
        elif opt in ("-c", "--count"):
            options["count"] = int(arg)
        elif opt in ("-r", "--roll"):
            methods = {
                "standard": pathfinder.ruleset.roll.STANDARD,
                "classic": pathfinder.ruleset.roll.CLASSIC,
                "heroic": pathfinder.ruleset.roll.HEROIC,
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
