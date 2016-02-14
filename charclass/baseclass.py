#! /usr/bin/env python
# -*- coding:utf-8 -*-


class CharClass():
    def __init__(self):
        self.alignments = [(x, y) for x in range(-1, 1) for y in range(-1, 1)]
        self.hd = (1, 8)
