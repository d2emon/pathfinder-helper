#! /usr/bin/env python
# -*- coding:utf-8 -*-


import sys
import random


def classes(id):
    if id == 100:
        return "Psionocs"
    elif id > 90:
        return "Monks"
    elif id > 80:
        return "Priests"
    elif id > 70:
        return "Wizards"
    elif id > 40:
        return "Thieves"
    else:
        return "Fighters"


def tributes(id):
    if id == 100:
        return "Tribute every month, either in the form of food, gifts or slaves"
    elif id > 87:
        return "Swear allegience to serve"
    elif id > 74:
        return "All of the towns wealth be given"
    elif id > 62:
        return "4 virgin girls be given"
    elif id > 50:
        return "The towns oldest person"
    elif id > 37:
        return "All of the towns gems be given"
    elif id > 25:
        return "10,000gp be given"
    elif id > 12:
        return "A virgin boy be given"
    else:
        return "A virgin girl be given"


def kidnapped(id):
    if id == 100:
        return "Men"
    elif id > 83:
        return "Girls"
    elif id > 66:
        return "Pets"
    elif id > 50:
        return "Women"
    elif id > 33:
        return "Boys"
    elif id > 17:
        return "Children"
    else:
        return "Elderly"


def fromFile(filename):
    adventures = []
    with open(filename) as f:
        adventures = f.readlines()
    return random.choice(adventures)


def main(argv):  # pragma: no cover
    files = {
        "tavern": "adventures/tavern.txt",
        "global": "adventures/global.txt",
        "local": "adventures/local.txt",
    }

    filename = files["local"]
    for a in argv[0:1]:
        filename = files.get(a, filename)

    quest = fromFile(filename)

    replaces = {
        "{{classes}}": classes(random.randrange(1, 101)),
        "{{tributes}}": tributes(random.randrange(1, 101)),
        "{{kidnapped}}": kidnapped(random.randrange(1, 101)),
    }
    for r in replaces.keys():
        quest = quest.replace(r, replaces[r])
    print(quest)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
