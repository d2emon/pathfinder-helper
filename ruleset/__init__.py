#! /usr/bin/env python
# -*- coding:utf-8 -*-


import ruleset.level
import ruleset.roll


class Ruleset():
    def __init__(self, **args):
        self.rollMethod = args.get("rollMethod", roll.STANDARD)
        self.levelUp = args.get("levelUp", level.NORMAL)
