#! /usr/bin/env python
# -*- coding:utf-8 -*-


import pathfinder.ruleset

DEBUG = False


def logOptions(options):
    import logging
    logger = logging.getLogger('helper')

    # Set log file name
    filename = options.get("-l")
    if filename is None:
        filename = options.get("--logfile")

    # Set log format
    logformat = "%(asctime)s: [%(levelname)s]:\t%(message)s"
    logformat = options.get("--logformat", logformat)

    config = dict()
    if filename is not None:
        config["filename"] = filename
        fh = logging.FileHandler(filename)
        logger.addHandler(fh)
    if logformat is not None:
        config["format"] = logformat

    print(config)
    # logging.basicConfig(**config)

    if DEBUG:
        debug_fh = logging.FileHandler('log/debug.log')
        debug_fh.setLevel(logging.DEBUG)
        logger.addHandler(debug_fh)

    logging.debug("Debug message")
    logging.error("Error message")


def parseArgs(argv, action=False):
    """
    Parsing argv for arguments
    """
    import getopt
    opts, args = getopt.getopt(argv, "hdl:c:r:f:", ["help", "debug", "logfile=", "count", "roll=", "file=", "logformat="])

    options = {opt: arg for opt, arg in opts}

    # Entering debug mode
    import os
    global DEBUG
    DEBUG = os.environ.get('DEBUG', DEBUG)
    if any(key in options.keys() for key in ("-d", "--debug")):
        DEBUG = True

    logOptions(options)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            raise getopt.GetoptError("")
        elif opt in ("-c", "--count"):
            options["count"] = int(arg)
        elif opt in ("-r", "--roll"):
            methods = {
                "standard": pathfinder.ruleset.roll.STANDARD,
                "classic": pathfinder.ruleset.roll.CLASSIC,
                "heroic": pathfinder.ruleset.roll.HEROIC,
            }
            options["rollMethod"] = methods[arg]
    if len(args) > 0:
        if action:
            options["action"] = args.pop(0)
        options["args"] = args

    return options
