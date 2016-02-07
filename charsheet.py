#! /usr/bin/env python
# -*- coding:utf-8 -*-


def showChar(char):
    print("Name: ", char.name)
    print("Alignment: ", char.alignment)
    print("Player: ", char.player)
    print("Class: ", char.charClass)
    print("Level: ", char.level)
    print("Deity: ", char.deity)
    print("Homeland: ", char.homeland)
    print("Race: ", char.race)
    print("Size: ", char.size)
    print("Gender: ", char.gender)
    print("Age: ", char.age)
    print("Height: ", char.height)
    print("Weight: ", char.weight)
    print("Hair: ", char.hair)
    print("Eyes: ", char.eyes)
    showAbilities(char)
    print("-" * 40)
    print("Cost: ", char.cost)


def showAbilities(char):
    for k in char.abilities:
        a = char.abilities[k]
        print("%s: %d (%d)" % (k, a.value, a.modifier))
