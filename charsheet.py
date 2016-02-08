#! /usr/bin/env python
# -*- coding:utf-8 -*-


def showChar(char):
    print("Name:\t", char.name)
    print("Align:\t", char.alignment)
    print("Player:\t", char.player)
    print("Class:\t%s(%d)" % (char.charClass, char.level))
    print("Deity:\t", char.deity)
    print("Home:\t", char.homeland)
    showRace(char.race)
    print("Size:\t", char.size)
    print("Gender:\t", ["?", "M", "F"][char.gender])
    print("Age:\t", char.age)
    print("Height:\t", char.height)
    print("Weight:\t", char.weight)
    print("Hair:\t", char.hair)
    print("Eyes:\t", char.eyes)
    showAbilities(char)
    print("-" * 40)
    print("Cost:\t", char.cost)


def showAbilities(char):
    for k in char.abilities:
        a = char.abilities[k]
        print("\t%s:\t%s" % (k, a))


def showRace(race):
    print("Race:\t", race.name)
    print("\tAbilities: ", race.abilities)
    print("\tSize: ", race.size)
    print("\tSpeed: ", race.speed)
    print("\tLowlight: ", race.lowlight)
    print("\tDarkvision: ", race.darkvision)
    print("\tWeapons: ", race.weapons, race.weaponGroups)
    print("\tLanguages: ", race.languages, race.additionalLanguages)
