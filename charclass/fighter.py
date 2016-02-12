#! /usr/bin/env python
# -*- coding:utf-8 -*-


import charclass
import charclass.charclass

BRB_ID = 101

print(charclass.charclass)
print(dir(charclass.charclass))


class Barbarian(charclass.charclass.CharClass):
    def __init__(self):
        self.alignments = [(x, y) for x in range(-1, 0) for y in range(-1, 1)]
        self.hd = (1, 12)
