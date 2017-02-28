#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Line:
    def __init__(self, s=""):
        self.data = s.strip()  # .encode('utf-8')


def LinesFile(filename):
    lines = []
    with open(filename, encoding='utf-8') as f:
        lines = [Line(s) for s in f.readlines()]
        return(lines)
