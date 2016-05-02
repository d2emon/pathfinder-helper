#! /usr/bin/env python
# -*- coding:utf-8 -*-


import random
import logging


def byPercent(cases=dict()):
    percents = list(cases.keys())
    percents.sort()

    p = random.randrange(100)
    logging.debug("%d%% of %s", p, percents)
    for i in percents:
        if p < i:
            return cases[i]


def d(dices=1, sides=6, dropMin=0, modifier=0):
    rolls = [Dice(sides) for d in range(dices)]

    rld = rolls[:]
    mns = []

    for i in range(dropMin):
        minDice = min(rolls)
        mns.append(minDice)
        rolls.remove(minDice)

    total = sum(d.result for d in rolls) + modifier
    logging.debug("%dd%d = %s-%s+%d = %d", dices, sides, rld, mns, modifier, total)
    return total


class Dice():
    def __init__(self, sides):
        self.sides = sides
        self.roll()

    def roll(self):
        self.result = random.randrange(1, self.sides+1)
        return self.result

    def __str__(self):
        return str(self.result)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.result < other.result
