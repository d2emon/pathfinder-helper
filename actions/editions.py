#! /usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import gui.menu

import actions.books

def pathfinder(id):
    r = gui.menu.showMenu(items=actions.books.PATHFINDER)
    print(r)
    r = gui.menu.showMenu(items=["{title} ({book})".format(
        title=u.get("title", "\u2026"),
        book=u.get("book", ""),
    ) for u in UNITS])
    print(r)
    return id


def dnd(id):
    r = gui.menu.showMenu(items=actions.books.DND3)
    print(r)
    return id


def cyclo(id):
    r = gui.menu.showMenu(items=actions.books.DND1)
    print(r)
    return id


UNITS = [
    {"title": "Pathfinder", "action": pathfinder},
    {"title": "DnD 3.5", "action": dnd},
    {"title": "Cyclopedia", "action": cyclo},
]


def selectBook(bookId):
    logging.debug("Book #%d", bookId)
    book = UNITS[bookId].get("action", None)
    return book(bookId)


def menu(actionId):
    r = gui.menu.showMenu(items=[u["title"] for u in UNITS], func=selectBook)
    logging.debug("Book: %s", r)
    return r
