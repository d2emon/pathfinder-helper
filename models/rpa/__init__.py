#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Campaign:
    def __init__(self, id=0, title="Campaign"):
        self.id = id
        self.title = title


class GameSystem:
    def __init__(self, id=0, name="RPG"):
        self.id = id
        self.name = name
        self.version = "7.13"
        self.path = self.name
        self.website = ""
        self.campaigns = []

        import random
        count = random.randrange(0, 10)
        for i in range(count):
            c_id = self.id * 16 + i
            c_title = "Campaign {}".format(i)
            self.campaigns.append(Campaign(c_id, c_title))


games = [
    GameSystem(1, "ADnD 2nd edition"),
    GameSystem(2, "ADnD 3rd edition"),
    GameSystem(3, "ADnD 3.5 edition"),
    GameSystem(4, "ADnD-Wyrms"),
]
