#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import ruleset
import abilities
import race
import charclass

import character.gender


STATS = {
    "STR": {"class": abilities.Ability, "dices": 3},
    "DEX": {"class": abilities.Ability, "dices": 3},
    "CON": {"class": abilities.Ability, "dices": 3},
    "INT": {"class": abilities.SpellAbility, "dices": 3},
    "WIS": {"class": abilities.Ability, "dices": 3},
    "CHA": {"class": abilities.Ability, "dices": 3},
}

VISION = {
    "normal": True,
    "low": 1,
    "dark": 0,
}


class Char():
    default = {
        "name": "Unnamed",
        "player": "Unknown",
        "alignment": None,
        "race": None,
        "charClass": [None],
        "favClass": [],
        "level": 0,
        "deity": "Unknown",
        "homeland": "Homeland",
        "size": 0,
        "gender": character.gender.UNKNOWN_ID,
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

        "ruleset": ruleset.Ruleset(),
    }

    def __init__(self, **args):
        logging.debug("Args are: %s", args)
        self.vision = args.get("vision", VISION.copy())
        for a in self.default:
            setattr(self, a, args.get(a, self.default[a]))

        self.abilities = dict()
        rollPool = dict()
        for s, d in STATS.items():
            print(s, "::", d)
            self.abilities[s] = d["class"]()
            rollPool[s] = d["dices"]
        if "rollPool" in args.keys():
            rollPool = args["rollPool"]

        stats = args.get("stats", None)
        logging.debug("Stats are: %s", stats)
        if stats is None:
            self.roll(rollPool)
            logging.debug("Stats are: %s", stats)
        elif isinstance(stats, dict):
            self.fill(**stats)
        else:
            self.fill(*stats)

        raceId = args.get("raceId", race.UNKNOWN_ID)
        self.race = race.raceById(raceId)

        classId = args.get("classId", charclass.UNKNOWN_ID)
        self.charclass = charclass.classById(classId)

    def roll(self, pool=None):
        [a.roll(self.ruleset.rollMethod) for a in self.abilities.values()]

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

    def getRace(self):
        return self.__race

    def setRace(self, value):
        self.__race = value
        if value is None:
            return
        for i, a in self.abilities.items():
            a.racialAdjustment = value.abilities.get(i, 0)

        logging.debug("V:%s", value)
        logging.debug("Vl:%s", value.lowlight)
        logging.debug("Vv:%s", self.vision)
        self.vision["low"] = value.lowlight
        self.vision["dark"] = value.darkvision

    def getCharClass(self):
        return self.__charClass

    def setCharClass(self, value):
        self.__charClass = value
        if value is None:
            return

        logging.debug("V:%s", value)
        logging.debug("Vv:%s", self.vision)

    cost = property(getCost)
    race = property(getRace, setRace)
    charClass = property(getCharClass, setCharClass)
