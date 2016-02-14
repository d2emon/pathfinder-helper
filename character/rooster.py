#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging

import character


class Rooster():
    def __init__(self, **args):
        import ruleset

        self.chars = args.get("chars", [])
        self.default = args.get("default", dict())
        if "ruleset" not in self.default.keys():
            self.default["ruleset"] = ruleset.Ruleset()

    def empty(self):
        self.chars = []


    def add(self, count=1, data=[], **default):
        charData = self.default.copy()
        charData.update(default)
        data = list(data) + [charData for i in range(len(data), count)]

        [self.chars.append(character.Char(**d)) for d in data]
        return self.chars

    def load(self, chars=[]):
        logging.debug("Rooster.load: %s", chars)
        [self.chars.append(character.Char(**c)) for c in chars]
        return self.chars

    def defineAbility(self, count=1, pool=None):
        logging.info("Determine Ability Scores")
        logging.debug("Rooster.defineAbility:Rules %s", self.default["ruleset"])
