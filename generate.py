#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import sys
import random

import gui
import gui.commandline
import ruleset
import race


import charsheet
import character.rooster
import charclass


def pickClass(chars=[], classes=[]):
    # TODO: Pick Class
    logging.info("Pick Your Class")
    return []


def pickSkills(chars=[]):
    # TODO: Pick Skills
    print("Pick Skills and Select Feats")
    return []


def buyEquipment(chars=[]):
    # TODO: Buy Equipment
    print("Buy Equipment")
    return []


def finishDetails(chars=[]):
    # TODO: Finish details
    print("Finishing Details")
    return []


def createChars(rooster=character.rooster.Rooster()):
    logging.debug("generate.createChars():Rooster %s", rooster)
    for c in rooster.chars:
        print("-" * 80)
        charsheet.showChar(c)
    print("-" * 80)
    for i in range(1, 11):
        l = charclass.Level(i)
        print("%d\t%d\t%s\t%s\t%s" % (i, l.toNext(), l.ability, l.skill, l.feat))
    l = charclass.xpToLevel(10000)
    print("%d\t%d\t%s\t%s\t%s" % (i, l.toNext(), l.ability, l.skill, l.feat))

    return rooster


def main(argv):  # pragma: no cover
    import getopt

    try:
        parsed = gui.commandline.parseArgs(argv)
    except(getopt.GetoptError):
        parsed = dict()
        gui.helpMessage()
    logging.info("Starting generator")

    ruleset.rules.rollMethod = parsed.get("rollMethod", gui.askRollMethod())
    filename = parsed.get("filename", None)
    count = parsed.get("count", None)
    if count is None:
        count = gui.askCharsCount()

    rooster = character.rooster.Rooster()
    rooster.load(filename)
    rooster.add(count=count)
    rooster.defineAbility()

    races = [random.choice(list(race.RACES.keys())) for i in rooster.chars]
    classes = [random.choice(list(charclass.CLASSES.keys())) for i in rooster.chars]

    logging.info("Pick Your Race")
    rooster.pickRace(races)
    logging.info("Pick Your Class")
    rooster.pickClass(classes)

    pickClass(rooster.chars, classes=[])
    pickSkills()
    buyEquipment()
    finishDetails()
    createChars(rooster)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
