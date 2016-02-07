#! /usr/bin/env python
# -*- coding:utf-8 -*-


import character
import abilities
import logging
import charsheet


def defineAbility():
    count = len(character.STATS)
    logging.info("Determine Ability Scores")
    data = {
        "name": "Test",
        "stats": [0, 13]
    }
    chars = [
        character.Char(name="Standard", stats=abilities.standard(count)),
        character.Char(name="Classic", stats=abilities.standard(count)),
        character.Char(name="Heroic", stats=abilities.standard(count)),
        character.Char(name="Pool", stats=abilities.standard(count)),
        character.Char(name="Pool", stats=abilities.pool([0, 3, 4, 5, 4, 3])),
        character.Char(**data),
    ]

    for c in chars:
        print("-" * 80)
        charsheet.showChar(c)
    print("-" * 80)

    return chars


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


def main():
    chars = defineAbility()
    pickRace()
    pickClass()
    pickSkills()
    buyEquipment()
    finishDetails()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s"
    )

    main()
