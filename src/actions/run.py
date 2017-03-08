#! /usr/bin/env python
# -*- coding:utf-8 -*-
import adventure
import equipment
import encounter
import generate

import actions.editions


CMDS = {
    "adventure": adventure.main,
    "equipment": equipment.main,

    "encounter": encounter.action,
    "generate": generate.action,
}


ACTIONS = [
    {"title": "Adventure", "action": CMDS["adventure"], "id": 1},
    {"title": "Art Object", "action": CMDS["equipment"], "id": 2},
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
    {"title": "Encounter", "action": CMDS["encounter"], "id": 19},
    {"title": "Generator", "action": CMDS["generate"], "id": 20},
    {"title": "Book", "action": actions.editions.menu, "id": 21},
]
