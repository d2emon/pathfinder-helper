#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging

import ruleset
import character


class Rooster():
    def __init__(self, **args):
        self.chars = args.get("chars", [])
        self.rules = args.get("rules", ruleset.Ruleset())

    def defineAbility(self, count=1, pool=None):
        logging.info("Determine Ability Scores")
        logging.debug("Rooster.defineAbility:Rules %s", self.rules)

    def add(self, count=1, data=[], **default):

        {"ruleset": self.rules}.update(default)

        data = list(data) + [default for i in range(len(data), count)]
        logging.debug("Rooster.add: %s", data)
        [self.chars.append(character.Char(**d)) for d in data]
        return self.chars

    def load(self, chars=[]):
        logging.debug("Rooster.load: %s", chars)
        [self.chars.append(character.Char(**c)) for c in chars]
        return self.chars
