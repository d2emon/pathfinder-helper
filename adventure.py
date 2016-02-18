#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging

import dice
import gui.commandline


CLASSES = {
    0: "Fighters",
    40: "Thieves",
    70: "Wizards",
    80: "Priests",
    90: "Monks",
    99: "Psionics",
}

TRIBUTES ={
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


FILES = {
    "tavern": "db/adventures/tavern.txt",
    "global": "db/adventures/global.txt",
    "local": "db/adventures/local.txt",
}


def fromFile(filename):
    import random

    adventures = []
    with open(filename) as f:
        adventures = f.readlines()
    return random.choice(adventures)


def main(id=0, options=[]):  # pragma: no cover
    logging.debug("Adventure generation")

    defaultId = "local"
    default = FILES[defaultId]
    if len(options) == 0:
        options.append(defaultId)
    filenames = [FILES.get(a, default) for a in options]
    quests = [fromFile(f) for f in filenames]

    replaces = {
        "{{classes}}": dice.byPercent(CLASSES),
        "{{tributes}}": dice.byPercent(TRIBUTES),
        "{{kidnapped}}": dice.byPercent(KIDNAPPED),
    }
    for q in quests:
        for r in replaces.keys():
            q = q.replace(r, replaces[r])
        print(q)


if __name__ == "__main__":  # pragma: no cover
    import sys
    import getopt

    try:
        options = gui.commandline.parseArgs(sys.argv[1:])
    except(getopt.GetoptError):
        gui.helpMessage()

    main(options=options.get("args", []))
