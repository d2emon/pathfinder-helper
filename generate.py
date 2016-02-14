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
    return []


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


def helpMessage():
    import sys
    # TODO: Help message
    print("Help!")
    sys.exit(0)


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


def parseArgs(argv):
    import getopt

    opts, args = getopt.getopt(argv, "hdl:c:r:f:", ["help", "debug", "logfile=", "count", "roll=", "file=", "logformat="])

    logconfig = {"format": "%(asctime)s: [%(levelname)s]:\t%(message)s"}
    options = {
        "rules": ruleset.Ruleset(),
    }
    print(opts, args)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            raise getopt.GetoptError("")
        elif opt in ("-d", "--debug"):
            logconfig["level"] = logging.DEBUG
        elif opt in ("-l", "--logfile"):
            logconfig["filename"] = arg
        elif opt in ("--logformat"):
            logconfig["format"] = arg
        elif opt in ("-c", "--count"):
            options["count"] = int(arg)
        elif opt in ("-r", "--roll"):
            methods = {
                "standard": ruleset.roll.STANDARD,
                "classic": ruleset.roll.CLASSIC,
                "heroic": ruleset.roll.HEROIC,
            }
            options["rules"].rollMethod = methods[arg]
        elif opt in ("-f", "--file"):
            with open(arg, "r") as f:
                options["chars"] = yaml.load(f)

    logging.basicConfig(**logconfig)
    return options


def main(argv):  # pragma: no cover
    import getopt

    try:
        parsed = parseArgs(argv)
    except(getopt.GetoptError):
        parsed = dict()
        helpMessage()

    chars = parsed.get("chars", [])
    count = parsed.get("count", 1) - len(chars)

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


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
