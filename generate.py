#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import sys
import yaml
import ruleset
import character
import race
import charclass
import charsheet


def defineAbility(count=1, rules=ruleset.Ruleset(), chars=[], pool=None):
    count -= len(chars)
    rooster = []

    logging.info("Determine Ability Scores")
    logging.debug("Loading %s", chars)
    for c in chars:
        rooster.append(character.Char(**c))
    logging.debug("%d character(s) left", count)
    logging.debug(rules)

    i = race.RACE_UNKNOWN
    rooster += [character.Char(
        name="Character %d" % (c),
        ruleset=rules,
        raceId=i + c + 1,
        dicePool=pool
    ) for c in range(count)]

    logging.debug(rooster)
    for c in rooster:
        print("-" * 80)
        charsheet.showChar(c)
    print("-" * 80)
    for i in range(1, 11):
        l = charclass.Level(i, rules)
        print("%d\t%d\t%s\t%s\t%s" % (i, l.toNext(), l.ability, l.skill, l.feat))
    l = charclass.xpToLevel(10000, rules)
    print("%d\t%d\t%s\t%s\t%s" % (i, l.toNext(), l.ability, l.skill, l.feat))

    return rooster


def pickClass():
    print("Pick Your Class")


def pickSkills():
    print("Pick Skills and Select Feats")


def buyEquipment():
    print("Buy Equipment")


def finishDetails():
    print("Finishing Details")


def helpMessage():
    # TODO: Help message
    print("Help!")


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

    logging.basicConfig(**logconfig)
    logging.info("Starting generator")

    chars = defineAbility(count=count, rules=rules, chars=chars)
    pickClass()
    pickSkills()
    buyEquipment()
    finishDetails()


if __name__ == "__main__":
    main(sys.argv[1:])
