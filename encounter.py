#! /usr/bin/env python
# -*- coding:utf-8 -*-


# import logging
import yaml
import random

import gui.menu


LAND_TYPES = []


class LandType():
    def __init__(self, data=""):
        pd = data.strip().rsplit("=")
        if len(pd) > 1:
            self.title = pd[1]
            self.groups = self.loadFromFile(pd[0])
        else:
            self.title = pd[0]
            self.groups = []

    def loadFromFile(self, filename):
        with open(filename) as f:
            return yaml.load(f)

    def randomGroup(self):
        group = random.choice(self.groups)
        filename = group.get("file", None)
        print(group)
        print(filename)
        if filename is not None:
            group.update(self.loadFromFile(filename))
        return group, random.choice(group["creatures"])


def getCreatureType(landType):
    try:
        l = LAND_TYPES[landType]
    except (IndexError):
        print(landType)
        raise ValueError
    g, c = l.randomGroup()
    print(l.title)
    return "%s(%s)" % (c, g["title"])


def main():
    global LAND_TYPES

    with open("db/lands.dat") as f:
        LAND_TYPES = [LandType(s) for s in f.readlines()]
    while True:
        cg = gui.menu.showMenu(items=[l.title for l in LAND_TYPES], func=getCreatureType)
        print(cg)


if __name__ == "__main__":
    main()
