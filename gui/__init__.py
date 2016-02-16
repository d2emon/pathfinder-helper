#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Gui methods
"""


# import logging
import gui.menu


def askCharsCount():
    """
    Asking of characters count
    """
    c = int(input("How many characters to create?\t"))
    return c


def askRollMethod():
    """
    Asking for roll method
    """
    def getMethod(index):
        import ruleset.roll
        methods = [
            ruleset.roll.STANDARD,
            ruleset.roll.CLASSIC,
            ruleset.roll.HEROIC,
        ]
        try:
            usePool = (index == 4)
            manual = (index == 5)
            return index, methods[index], usePool, manual
        except (IndexError):
            raise ValueError

    s, m, usePool, manual = gui.menu.showMenu(
        title="Select roll method:",
        items=[
            "Standard",
            "Classic",
            "Heroic",
            "Dice pool",
            "Manual",
        ],
        func=getMethod
    )
    return m


def bye():
    """
    Shutting down
    """
    import sys

    print("Bye!")
    sys.exit(0)


def helpMessage():
    """
    Showing help message
    """
    # TODO: Help message
    print("Help!")
    bye()
