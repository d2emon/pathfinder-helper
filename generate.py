#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import yaml
import character
import abilities
import charsheet
import race


def defineAbility():
    count = len(character.STATS)
    logging.info("Determine Ability Scores")
    with open("test.yml", "r") as f:
        data = yaml.load(f)
    print(data)
    pool = {
        "STR": 3,
        "CON": 4,
        "INT": 5,
        "WIS": 6,
    }
    chars = [
        character.Char(
            name="Stnd",
            rollMethod=abilities.ROLL_STANDARD,
            raceId=race.RACE_DWARF,
        ),
        character.Char(
            name="Clas",
            rollMethod=abilities.ROLL_CLASSIC,
            raceId=race.RACE_ELF,
        ),
        character.Char(
            name="Hero",
            rollMethod=abilities.ROLL_HEROIC,
            raceId=race.RACE_GNOME,
        ),
        character.Char(
            name="Pool",
            rollPool=pool,
            raceId=race.RACE_HALFELF,
        ),
        character.Char(
            name="Pool",
            rollPool=pool,
            raceId=race.RACE_HALFLING,
        ),
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
