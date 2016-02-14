#! /usr/bin/env python
# -*- coding:utf-8 -*-


import charclass.baseclass

BRB_ID = 101

print(charclass.baseclass)
print(dir(charclass.baseclass))


class Barbarian(charclass.baseclass.CharClass):
    def __init__(self):
        self.alignments = [(x, y) for x in range(-1, 0) for y in range(-1, 1)]
        self.hd = (1, 12)
