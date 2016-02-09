#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import abilities
import race


GENDER_UNKNOWN = 0
GENDER_MALE = 1
GENDER_FEMALE = 2

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
    "dim": 1,
    "dark": 0,
}


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

        "rollMethod": abilities.ROLL_CLASSIC,
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

        raceId = args.get("raceId", race.RACE_UNKNOWN)
        self.race = race.raceById(raceId)

    def roll(self, pool=None):
        [a.roll(self.rollMethod) for a in self.abilities.values()]

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

        logging.debug(value)
        logging.debug(value.lowlight)
        logging.debug(self.vision)
        self.vision["low"] = value.lowlight
        self.vision["dark"] = value.darkvision

    cost = property(getCost)
    race = property(getRace, setRace)
