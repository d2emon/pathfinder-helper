#! /usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import gui

import adventure
import equipment
import encounter
import generate

import actions.editions


CMDS = {
    "adventure": adventure.main,
    "equipment": equipment.main,

    "encounter": encounter.main,
    "generate": generate.action,
}


ACTIONS = [
    {"title": "Adventure", "action": CMDS["adventure"]},
    {"title": "Art Object", "action": CMDS["equipment"]},
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
    {"title": "Encounter", "action": CMDS["encounter"]},
    {"title": "Generator", "action": CMDS["generate"]},
    {"title": "Book", "action": actions.editions.menu},
]


def action(action=None, args=[]):
    if action is None:
        return 0

    a = CMDS.get(action, None)
    logging.debug("Running %s", action)
    if a is None:
        gui.helpMessage()
    a(0, args)

    import sys
    sys.exit(0)


def byId(actionId):
    a = ACTIONS[actionId].get("action", None)
    if a is not None:
        return a(actionId)
    return actionId

