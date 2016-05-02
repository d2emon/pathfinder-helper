#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging


def main(id=0, options=dict()):  # pragma: no cover
    """
    Main helper function
    """
    import gui.menu
    import actions

    logging.info("Starting helper")
    actions.runAction(action=options.get("action", None), args=options.get("args", []))

    while True:
        gui.menu.showMenu(items=actions.ACTIONS, func=actions.runById)


if __name__ == "__main__":  # pragma: no cover
    import sys
    import getopt
    import gui.commandline

    try:
        options = gui.commandline.parseArgs(sys.argv[1:], action=True)
    except(getopt.GetoptError):
        gui.helpMessage()

    main(options=options)
