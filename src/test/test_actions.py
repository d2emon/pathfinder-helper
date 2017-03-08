#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Testing actions
"""

import unittest
import actions.run
import actions.editions


class TestActions(unittest.TestCase):
    def testNoAction(self):
        '''
        Ensure that returns False on no action
        '''
        self.assertFalse(actions.run.action(action=None, args=[]))


    def testBadAction(self):
        '''
        Ensure that returns False on bad action
        '''
        self.assertFalse(actions.run.action(action="bad_action", args=[]))


    def testAdventureAction(self):
        '''
        Ensure that returns False on adventure
        '''
        self.assertFalse(actions.run.action(action='adventure', args=[]), "Wrong adventure action")


    def testEquipmentAction(self):
        '''
        Ensure that returns False on equipment
        '''
        self.assertFalse(actions.run.action(action='equipment', args=[]), "Wrong equipment action")


    def testEncounterAction(self):
        '''
        Ensure that returns False on encounter
        '''
        self.assertFalse(actions.run.action(action='encounter', args=[]), "Wrong encounter action")


    def testGenerateAction(self):
        '''
        Ensure that returns False on generate
        '''
        self.assertFalse(actions.run.action(action='generate', args=[]), "Wrong generate action")


    def testByIdNegative(self):
        '''
        Ensure that returns False on negative action id
        '''
        self.assertFalse(actions.run.byId(-1))


    def testByIdPositive(self):
        '''
        Ensure that returns False on positive action id
        '''
        import random
        action_id = random.randint(0, len(actions.run.ACTIONS))
        self.assertEquals(actions.run.byId(action_id), action_id)


    def testByIdBig(self):
        '''
        Ensure that returns False on big action id
        '''
        self.assertFalse(actions.run.byId(256))


    def testPathfinder(self):
        '''
        Ensure that returns False using Pathfinder
        '''
        import random
        self.assertFalse(actions.editions.pathfinder(random.randint(-255, 255)))


    def testDnd(self):
        '''
        Ensure that returns False using DnD
        '''
        import random
        self.assertFalse(actions.editions.dnd(random.randint(-255, 255)))


    def testCyclo(self):
        '''
        Ensure that returns False using Cyclo
        '''
        import random
        self.assertFalse(actions.editions.cyclo(random.randint(-255, 255)))


    def testBookSelection(self):
        '''
        Ensure that returns False on selecting book
        '''
        import random
        self.assertFalse(actions.editions.selectBook(random.randint(-255, 255)))


    def testMenu(self):
        '''
        Ensure that returns False on entering menu
        '''
        import random
        self.assertFalse(actions.editions.menu(random.randint(-255, 255)))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
