#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging

import gui
import gui.commandline
import actions


def main(id=0, options=dict()):  # pragma: no cover
    logging.info("Starting helper")
    actions.runAction(action=options.get("action", None), args=options.get("args", []))

    while True:
        r = gui.menu.showMenu(items=[a["title"] for a in actions.ACTIONS], func=actions.runById)
        print(r)


if __name__ == "__main__":  # pragma: no cover
    import sys
    import getopt

    try:
        options = gui.commandline.parseArgs(sys.argv[1:], action=True)
    except(getopt.GetoptError):
        gui.helpMessage()

    main(options=options)
