#! /usr/bin/env python
# -*- coding:utf-8 -*-


import dice

import ruleset.level
import ruleset.roll


class Ruleset():
    def __init__(self, **args):
        self.rollMethod = args.get("rollMethod", ruleset.roll.STANDARD)
        self.levelUp = args.get("levelUp", ruleset.level.NORMAL)

    def rollAbility(self, ability, pool):
        ability.value = dice.d(**self.rollMethod)


rules = Ruleset()
