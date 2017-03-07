#! /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import actions.run


class TestActions(unittest.TestCase):
    def testNoAction(self):
        '''
        Ensure that main loop runs
        '''
        self.assertFalse(actions.run.action(action=None, args=[]), "Main loop")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
