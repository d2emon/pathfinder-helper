#! /usr/bin/env python
# -*- coding:utf-8 -*-


import character
import abilities
import logging
import charsheet


def defineAbility(char):
    logging.info("Determine Ability Scores")

    l = abilities.standard(char)
    char.fill(*l)
    logging.info("Standard %s - %s", l, char.abilities)
    logging.info(char.cost)
    charsheet.showChar(char)

    l = abilities.classic(char)
    char.fill(*l)
    logging.info("Classic %s - %s", l, char.abilities)
    logging.info(char.cost)
    charsheet.showChar(char)

    l = abilities.heroic(char)
    char.fill(*l)
    logging.info("Heroic %s - %s", l, char.abilities)
    logging.info(char.cost)
    charsheet.showChar(char)

    l = abilities.pool(char, [0, 3, 4, 5, 4, 3])
    char.fill(*l)
    logging.info("Pool %s - %s", l, char.abilities)
    logging.info(char.cost)
    charsheet.showChar(char)


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
    char = character.Char()
    defineAbility(char)
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
