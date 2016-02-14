#! /usr/bin/env python
# -*- coding:utf-8 -*-


import ruleset
import charclass.baseclass
import charclass.fighter


class Level():
    def __init__(self, level=0, ruleset=ruleset.Ruleset()):
        self.level = level
        self.ruleset = ruleset

    def toNext(self):
        return self.ruleset.levelUp[self.level]

    def getFeat(self):
        return (self.level % 2) == 1

    def getSkill(self):
        return True

    def getAbility(self):
        return (self.level % 4) == 0

    feat = property(getFeat)
    skill = property(getSkill)
    ability = property(getAbility)


def xpToLevel(xp, ruleset=ruleset.Ruleset()):
    for l, tolup in enumerate(ruleset.levelUp):
        if xp < tolup:
            return Level(l, ruleset)


UNKNOWN_ID = 0


def classById(id):
    return CLASSES.get(id, charclass.baseclass.CharClass)()


CLASSES = {
    charclass.fighter.BRB_ID: charclass.fighter.Barbarian(),
}
