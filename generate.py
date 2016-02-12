#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import sys
import yaml

import ruleset
import race


import charsheet
import character.rooster
import charclass


def pickRace(chars=[], races=[]):
    logging.info("Pick Your Race")
    races = list(races) + [race.UNKNOWN_ID] * (len(chars) - len(races))
    for i, c in enumerate(chars):
        c.race = race.raceById(races[i])


def pickClass(chars=[], classes=[]):
    # TODO: Pick Class
    logging.info("Pick Your Class")


def pickSkills():
    # TODO: Pick Skills
    print("Pick Skills and Select Feats")


def buyEquipment():
    # TODO: Buy Equipment
    print("Buy Equipment")


def finishDetails():
    # TODO: Finish details
    print("Finishing Details")


def helpMessage():
    # TODO: Help message
    print("Help!")


def createChars(rooster=character.rooster.Rooster(), rules=ruleset.ruleset.Ruleset()):
    logging.debug("generate.createChars():Rooster %s", rooster)
    for c in rooster.chars:
        print("-" * 80)
        charsheet.showChar(c)
    print("-" * 80)
    for i in range(1, 11):
        l = charclass.Level(i, rules)
        print("%d\t%d\t%s\t%s\t%s" % (i, l.toNext(), l.ability, l.skill, l.feat))
    l = charclass.xpToLevel(10000, rules)
    print("%d\t%d\t%s\t%s\t%s" % (i, l.toNext(), l.ability, l.skill, l.feat))

    return rooster


def main(argv):
    import getopt

    try:
        opts, args = getopt.getopt(argv, "hdl:c:r:f:", ["help", "debug", "logfile=", "count", "roll=", "file=", "logformat"])
    except(getopt.GetoptError):
        opts = ("-h", "")

    logconfig = {"format": "%(asctime)s: [%(levelname)s]:\t%(message)s"}
    count = 1
    rules = ruleset.Ruleset()
    chars = []
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            helpMessage()
        elif opt in ("-d", "--debug"):
            logconfig["level"] = logging.DEBUG
        elif opt in ("-l", "--logfile"):
            logconfig["filename"] = arg
        elif opt in ("--logformat"):
            logconfig["format"] = arg
        elif opt in ("-c", "--count"):
            count = int(arg)
        elif opt in ("-r", "--roll"):
            methods = {
                "standard": ruleset.roll.STANDARD,
                "classic": ruleset.roll.CLASSIC,
                "heroic": ruleset.roll.HEROIC,
            }
            rules.rollMethod = methods[arg]
        elif opt in ("-f", "--file"):
            with open(arg, "r") as f:
                chars = yaml.load(f)
    count -= len(chars)

    logging.basicConfig(**logconfig)
    logging.info("Starting generator")
    logging.debug("generate:Chars %s", chars)

    rooster = character.rooster.Rooster()
    rooster.add(count=count)
    pickRace(rooster.chars, races=race.RACES.keys())
    pickClass(rooster.chars, classes=[])
    pickSkills()
    buyEquipment()
    finishDetails()
    rooster.load(chars)
    createChars(rooster)


if __name__ == "__main__":
    main(sys.argv[1:])
