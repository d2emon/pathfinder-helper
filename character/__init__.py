#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import abilities


GENDER_UNKNOWN = 0
GENDER_MALE = 1
GENDER_FEMALE = 2

STATS = [
    "STR",
    "DEX",
    "CON",
    "INT",
    "WIS",
    "CHA",
]


class Char():
    default = {
        "name": "Unnamed",
        "player": "Unknown",
        "alignment": None,
        "race": None,
        "charClass": None,
        "level": 0,
        "deity": "Unknown",
        "homeland": "Homeland",
        "size": 0,
        "gender": GENDER_UNKNOWN,
        "age": 0,
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
        logging.debug("Args are: %s", args)
        for a in self.default:
            setattr(self, a, args.get(a, self.default[a]))
        self.abilities = {
            "STR": abilities.Ability(),
            "DEX": abilities.Ability(),
            "CON": abilities.Ability(),
            "INT": abilities.SpellAbility(),
            "WIS": abilities.Ability(),
            "CHA": abilities.Ability(),
        }
        self.fill(*args.get("stats", []))

    def fill(self, *stats, **named):
        logging.debug("Stats are: %s", stats)
        st = list(stats)
        st += [0] * (len(self.abilities) - len(st))
        logging.debug("Stats are: %s", st)

        for i, a in enumerate(self.abilities.keys()):
            self.abilities[a].value = named.get(a, st[i])
        logging.debug("Abilities are: %s", self.abilities)

    def getCost(self):
        stats = [s.cost for s in self.abilities.values()]
        logging.debug("Character cost is %d(%s)", sum(stats), " + ".join([str(s) for s in stats]))
        return sum(stats)

    cost = property(getCost)
