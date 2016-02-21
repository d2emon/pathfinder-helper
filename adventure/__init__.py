#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging

import dice
import gui.menu


CLASSES = {
    0: "Fighters",
    40: "Thieves",
    70: "Wizards",
    80: "Priests",
    90: "Monks",
    99: "Psionics",
}

TRIBUTES = {
    99: "Tribute every month, either in the form of food, gifts or slaves",
    87: "Swear allegience to serve",
    74: "All of the towns wealth be given",
    62: "4 virgin girls be given",
    50: "The towns oldest person",
    37: "All of the towns gems be given",
    25: "10,000gp be given",
    12: "A virgin boy be given",
    0: "A virgin girl be given",
}

KIDNAPPED = {
    99: "Men",
    83: "Girls",
    66: "Pets",
    50: "Women",
    33: "Boys",
    17: "Children",
    0: "Elderly",
}


FILENAMES = {
    "tavern": "db/adventures/tavern.txt",
    "global": "db/adventures/global.txt",
    "local": "db/adventures/local.txt",
}

STYLES = [
    {"title": "Local", "filename": FILENAMES["local"]},
    {"title": "Tavern", "filename": FILENAMES["tavern"]},
    {"title": "Global", "filename": FILENAMES["global"]},
]


class Adventure():
    def __init__(self, style):
        self.description = ""
        logging.debug(style)
        self.title = style.get("title", None)
        filename = style.get("filename", None)
        if filename is not None:
            self.load(filename)

    def load(self, filename):
        import random

        adventures = []
        with open(filename) as f:
            adventures = f.readlines()
        self.description = random.choice(adventures).rstrip()


def selStyle(id, args=[]):
    style = STYLES[id]
    return style


def main(id=0, options=[]):  # pragma: no cover
    logging.debug("Adventure generation")

    default = FILENAMES["local"]
    logging.debug(options)
    adventures = []
    if len(options) == 0:
        adventures = [Adventure(style=gui.menu.showMenu(title="Select adventure type:", items=[s["title"] for s in STYLES], func=selStyle))]
    else:
        adventures = [Adventure(style={"filename": FILENAMES.get(a, default)}) for a in options]

    replaces = {
        "{{classes}}": dice.byPercent(CLASSES),
        "{{tributes}}": dice.byPercent(TRIBUTES),
        "{{kidnapped}}": dice.byPercent(KIDNAPPED),
    }
    for q in adventures:
        for r in replaces.keys():
            q.description = q.description.replace(r, replaces[r])
        print(q.title)
        print(q.description)


if __name__ == "__main__":  # pragma: no cover
    import sys
    import getopt
    import gui
    import gui.commandline

    try:
        options = gui.commandline.parseArgs(sys.argv[1:])
    except(getopt.GetoptError):
        gui.helpMessage()

    main(options=options.get("args", []))
