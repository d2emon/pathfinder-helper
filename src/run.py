#! /usr/bin/env python
# -*- coding:utf-8 -*-
def main(id=0, options=dict()):  # pragma: no cover
    """
    Main helper function
    """
    import logging
    import gui.menu
    import actions.run

    logging.info("Starting helper")
    actions.run.action(action=options.get("action", None), args=options.get("args", []))

    while True:
        gui.menu.showMenu(items=actions.run.ACTIONS, func=actions.run.byId)


if __name__ == "__main__":  # pragma: no cover
    import sys
    import getopt
    import gui.commandline

    try:
        options = gui.commandline.parseArgs(sys.argv[1:], action=True)
    except(getopt.GetoptError):
        gui.helpMessage()

    main(options=options)
