#! /usr/bin/env python
# -*- coding:utf-8 -*-


import random
import logging


def d(dices=1, sides=6, dropMin=0, modifier=0):
    dices = [Dice(sides) for d in range(dices)]
    logging.debug("You've rolled %s", dices)

    for i in range(dropMin):
        minDice = min(dices)
        logging.debug("Removing minimal dice(%s)", minDice)
        dices.remove(minDice)

    total = sum(d.result for d in dices) + modifier
    logging.debug("Total dices is %d from %s plus %d", total, dices, modifier)
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
