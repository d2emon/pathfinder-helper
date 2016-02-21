#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging

import gui
import adventure
import generate
import encounter


PATHFINDER = [
    {"book": "PathC", "title": "1.Getting Started"},
    {"book": "PathC", "title": "2.Races"},
    {"book": "PathC", "title": "3.Classes"},
    {"book": "PathC", "title": "4.Skills"},
    {"book": "PathC", "title": "5.Feats"},
    {"book": "PathC", "title": "6.Equipment"},
    {"book": "PathC", "title": "7.Additional"},
    {"book": "PathC", "title": "8.Combat"},
    {"book": "PathC", "title": "9.Magic"},
    {"book": "PathC", "title": "10.Spells"},
    {"book": "PathC", "title": "11.Prestige Classes"},
    {"book": "PathC", "title": "12.Gamemastering"},
    {"book": "PathC", "title": "13.Environment"},
    {"book": "PathC", "title": "14.Creating NPC"},
    {"book": "PathC", "title": "15.Magic Items"},
    {"book": "PathC", "title": "A1.Special Abilities"},
    {"book": "PathC", "title": "A2.Conditions"},

    {"book": "PathA", "title": "1.Races"},
    {"book": "PathA", "title": "2.Classes"},
    {"book": "PathA", "title": "3.Feats"},
    {"book": "PathA", "title": "4.Equipment"},
    {"book": "PathA", "title": "5.Spells"},
    {"book": "PathA", "title": "6.Magic Items"},
    {"book": "PathA", "title": "7.New Rules"},
]

DND3 = [
    {"book": "PHB", "title": "1.Abilities"},
    {"book": "PHB", "title": "2.Races"},
    {"book": "PHB", "title": "3.Classes"},
    {"book": "PHB", "title": "4.Skills"},
    {"book": "PHB", "title": "5.Feats"},
    {"book": "PHB", "title": "6.Desription"},
    {"book": "PHB", "title": "7.Equipment"},
    {"book": "PHB", "title": "8.Combat"},
    {"book": "PHB", "title": "9.Adventuring"},
    {"book": "PHB", "title": "10.Magic"},
    {"book": "PHB", "title": "11.Spells"},

    {"book": "PHB2", "title": "1.New Classes"},
    {"book": "PHB2", "title": "2.Expanded Classes"},
    {"book": "PHB2", "title": "3.New Feats"},
    {"book": "PHB2", "title": "4.New Spells"},
    {"book": "PHB2", "title": "5.Identity"},
    {"book": "PHB2", "title": "6.Group"},
    {"book": "PHB2", "title": "7.Affilations"},
    {"book": "PHB2", "title": "8.Rebuilding"},
    {"book": "PHB2", "title": "A.Quick Creation"},

    {"book": "DMG", "title": "1.Game"},
    {"book": "DMG", "title": "2.Rules"},
    {"book": "DMG", "title": "3.Adventures"},
    {"book": "DMG", "title": "4.NPC"},
    {"book": "DMG", "title": "5.Campaigns"},
    {"book": "DMG", "title": "6.Characters"},
    {"book": "DMG", "title": "7.Magic Items"},
    {"book": "DMG", "title": "8.Glossary"},

    {"book": "DMG2", "title": "1.Game"},
    {"book": "DMG2", "title": "2.Adventures"},
    {"book": "DMG2", "title": "3.Campaigns"},
    {"book": "DMG2", "title": "4.Saltmarsh"},
    {"book": "DMG2", "title": "5.NPC"},
    {"book": "DMG2", "title": "6.Characters"},
    {"book": "DMG2", "title": "7.Magic Items"},
]

DND1 = [
    {"book": "Cycl", "title": "1.Steps"},
    {"book": "Cycl", "title": "2.Classes"},
    {"book": "Cycl", "title": "3.Spells"},
    {"book": "Cycl", "title": "4.Equipment"},
    {"book": "Cycl", "title": "5.Other"},
    {"book": "Cycl", "title": "6.Movement"},
    {"book": "Cycl", "title": "7.Encounters"},
    {"book": "Cycl", "title": "8.Combat"},
    {"book": "Cycl", "title": "9.Mass Combat"},
    {"book": "Cycl", "title": "10.Experience"},
    {"book": "Cycl", "title": "11.Creating NPC"},
    {"book": "Cycl", "title": "12.Strongholds"},
    {"book": "Cycl", "title": "13.Gamemastering"},
    {"book": "Cycl", "title": "14.Monsters"},
    {"book": "Cycl", "title": "15.Immortals"},
    {"book": "Cycl", "title": "16.Treasure"},
    {"book": "Cycl", "title": "17.Environment"},
    {"book": "Cycl", "title": "18.Planes"},
    {"book": "Cycl", "title": "19.Variant"},
    {"book": "Cycl", "title": "A1.World"},
    {"book": "Cycl", "title": "A2.Conversions"},
    {"book": "Cycl", "title": "A3.Record Sheets"},

    {"book": "CRB", "title": "FastNPC"},
    {"book": "CRB", "title": "Campaign"},
    {"book": "CRB", "title": "World"},
    {"book": "CRB", "title": "Plots"},
    {"book": "CRB", "title": "Primary NPC"},
    {"book": "CRB", "title": "Secondary NPC"},
    {"book": "CRB", "title": "PC"},
    {"book": "CRB", "title": "Maps"},
    {"book": "CRB", "title": "Calendar"},
    {"book": "CRB", "title": "Log"},
    {"book": "CRB", "title": "Random Encounters"},
    {"book": "CRB", "title": "Homerules"},
    {"book": "CRB", "title": "Pockets"},
    {"book": "CRB", "title": "Tavern"},
]


def pathfinder(id):
    r = gui.menu.showMenu(items=PATHFINDER)
    print(r)
    r = gui.menu.showMenu(items=["{title} ({book})".format(
        title=u.get("title", "\u2026"),
        book=u.get("book", ""),
    ) for u in UNITS])
    print(r)
    return id


def dnd(id):
    r = gui.menu.showMenu(items=DND3)
    print(r)
    return id


def cyclo(id):
    r = gui.menu.showMenu(items=DND1)
    print(r)
    return id


UNITS = [
    {"title": "Generator", "action": generate.main},
    {"title": "Encounter", "action": encounter.main},
    {"title": "Pathfinder", "action": pathfinder},
    {"title": "DnD 3.5", "action": dnd},
    {"title": "Cyclopedia", "action": cyclo},
]


def selectBook(bookId):
    logging.debug("Book #%d", bookId)
    book = UNITS[bookId].get("action", None)
    return book(bookId)


def booksMenu(actionId):
    r = gui.menu.showMenu(items=[u["title"] for u in UNITS], func=selectBook)
    logging.debug("Book: %s", r)
    return r


CMDS = {
    "adventure": adventure.main
}


ACTIONS = [
    {"title": "Adventure", "action": CMDS["adventure"]},
    {"title": "Art Object"},
    {"title": "Attribute"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure", "action": booksMenu},
]


def runById(actionId):
    a = ACTIONS[actionId].get("action", None)
    if a is not None:
        return a(actionId)
    return actionId


def runAction(action=None, args=[]):
    if action is None:
        return 0

    a = CMDS.get(action, None)
    logging.debug("Running %s", action)
    if a is None:
        gui.helpMessage()
    a(0, args)

    import sys
    sys.exit(0)
