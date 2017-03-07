#! /usr/bin/env python
# -*- coding:utf-8 -*-


import unittest
import random

import character.rooster


class TestRooster(unittest.TestCase):
    def setUp(self):
        self.rooster = character.rooster.Rooster()

    def testOtherRuleset(self):
        '''
        Ensure that rooster get proper ruleset
        '''
        import ruleset

        rs = ruleset.Ruleset(rollMethod=random.choice([
            ruleset.roll.CLASSIC,
            ruleset.roll.STANDARD,
            ruleset.roll.HEROIC,
        ]))
        r = character.rooster.Rooster(default={"ruleset": rs})
        self.assertEqual(r.default["ruleset"], rs)

    def testAdd(self):
        '''
        Ensure that one character is added
        '''
        self.rooster.empty()
        self.rooster.add()
        self.assertEqual(len(self.rooster.chars), 1)

    def testAddCount(self):
        '''
        Ensure that some characters are added
        '''
        count = random.randrange(10)
        self.rooster.empty()
        self.rooster.add(count)
        self.assertEqual(len(self.rooster.chars), count)

    def testLoad(self):
        '''
        Ensure that some character are loaded
        '''
        count = random.randrange(10)
        chars = [{
            "name": "Character%d" % (i)
        } for i in range(count)]
        self.rooster.empty()
        self.rooster.load(chars)
        self.assertEqual(len(self.rooster.chars), count)
        [self.assertEqual(self.rooster.chars[i].name, chars[i]["name"]) for i in range(count)]

    def testDefineAbility(self):
        r = self.rooster.defineAbility()
        self.assertEqual(r, 10)
