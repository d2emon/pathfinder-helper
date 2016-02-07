#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import abilities


GENDER_UNKNOWN = 0
GENDER_MALE = 1
GENDER_FEMALE = 2


class Char():
    abilityNames = (
        "STR",
        "DEX",
        "CON",
        "INT",
        "WIS",
        "CHA",
    )
    abilities = [None] * len(abilityNames)
    default = {
        "name": "Unnamed",
        "player": "Unknown",
        "alignment": None,
        "race": None,
        "class": None,
        "level": 0,
        "deity": "Unknown",
        "homeland": "Homeland",
        "size": 0,
        "gender": GENDER_UNKNOWN,
        "height": 0,
        "weight": 0,
        "hair": "Unknown",
        "eyes": "Unknown",
        "hp": 0,
        "initiative": 0,
        "speed": 0,
        "skills": [],
        "ac": 0,
        "savingThrows": [],
        "bab": 0,
        "spellResistance": 0,
        "cmb": 0,
        "cmd": 0,
        "weapons": [],
        "languages": [],
    }

    def __init__(self, **args):
        for a in self.default:
            setattr(self, a, args.get(a, self.default[a]))
        self.fill(*args.get("stats", []))

    def fill(self, *stats):
        st = list(stats)
        l = len(self.abilityNames) - len(st)
        st += [0] * l

        a = [[abilities.Ability(s), abilities.SpellAbility(s)][i == 3] for i, s in enumerate(st)]
        self.abilities = dict(zip(self.abilities, a))

    def getCost(self):
        stats = [s.cost for s in self.abilities.values()]
        logging.debug("Character cost is %d(%s)", sum(stats), " + ".join([str(s) for s in stats]))
        return sum(stats)

    cost = property(getCost)
