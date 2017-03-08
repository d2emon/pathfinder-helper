#! /usr/bin/env python
# -*- coding:utf-8 -*-


from actions.run import ACTIONS
from actions.run import CMDS


def runAction(action, *args):
    if action is None:
        return False

    import logging
    logging.debug("Running %s", action)

    cmd = CMDS.get(action, None)
    if cmd is None:
        return False

    cmd(0, *args)
    return True


def runById(actionId):
    action = ACTIONS[actionId].get("action", None)
    if action is None:
        return False  # actionId
    return action(actionId)
