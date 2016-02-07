#! /usr/bin/env python
# -*- coding:utf-8 -*-


import dice


def standard(char):
    return [dice.d(4, 6, dropMin=1) for a in char.abilities]


def classic(char):
    return [dice.d(3, 6) for a in char.abilities]


def heroic(char):
    return [dice.d(2, 6, modifier=6) for a in char.abilities]


def pool(char, dices):
    return [dice.d(max(n, 3), 6) for n in dices]


def purchase():
    return 4


class Ability():
    minValue = 3
    maxValue = 18
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.isSet = value is not None

        if not self.isSet:
            value = 0

        if value < self.minValue:
            self.__value = self.minValue
        elif value > self.maxValue:
            self.__value = self.maxValue
        else:
            self.__value = value

    def getCost(self):
        if self.value > 16:
            return 4 * (self.value - 14) + 1
        elif self.value > 14:
            return 3 * (self.value - 13) + 1
        elif self.value > 12:
            return 2 * (self.value - 12) + 1
        elif self.value > 7:
            return (self.value - 11) + 1
        else:
            return -4

    def getModifier(self):
        return int(self.value / 2) - 5

    def __str__(self):
        return "%s(%d)" % ([None, self.value][self.isSet], self.modifier)

    def __repr__(self):
        return self.__str__()

    cost = property(getCost)
    modifier = property(getModifier)


class SpellAbility(Ability):
    def getSpells(self):
        m = self.modifier
        spells = [[0, int((m - i - 1) / 4) + 1][i < m] for i in range(9)]
        return [0] + spells

    def canSpell(self):
        return self.value >= 10

    def __str__(self):
        return "%s(%d):%s" % ([None, self.value][self.isSet], self.modifier, [None, self.spells][self.canSpell()])

    spells = property(getSpells)
