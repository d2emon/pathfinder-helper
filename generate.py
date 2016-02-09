#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import sys
import yaml
import character
import abilities
import charsheet
import race


def defineAbility(count=1, method=abilities.ROLL_STANDARD, chars=[], pool=None):
    count -= len(chars)
    rooster = []

    logging.info("Determine Ability Scores")
    logging.debug("Loading %s", chars)
    for c in chars:
        rooster.append(character.Char(**c))
    logging.debug("%d character(s) left", count)
    logging.debug(method)

    i = race.RACE_UNKNOWN
    rooster += [character.Char(
        name="Character %d" % (c),
        rollMethod=method,
        raceId=i + c + 1,
        dicePool=pool
    ) for c in range(count)]

    logging.debug(rooster)
    for c in rooster:
        print("-" * 80)
        charsheet.showChar(c)
    print("-" * 80)

    return rooster


def pickRace():
    print("Pick Your Race")


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
    method = abilities.ROLL_STANDARD
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
                "standard": abilities.ROLL_STANDARD,
                "classic": abilities.ROLL_CLASSIC,
                "heroic": abilities.ROLL_HEROIC,
            }
            method = methods[arg]
        elif opt in ("-f", "--file"):
            with open(arg, "r") as f:
                chars = yaml.load(f)

    logging.basicConfig(**logconfig)
    logging.info("Starting generator")

    chars = defineAbility(count=count, method=method, chars=chars)
    pickRace()
    pickClass()
    pickSkills()
    buyEquipment()
    finishDetails()


if __name__ == "__main__":
    main(sys.argv[1:])
