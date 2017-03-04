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
        self.path = "db"
        self.website = ""
        self.campaigns = []

        import random
        count = random.randrange(0, 10)
        for i in range(count):
            c_id = self.id * 16 + i
            c_title = "Campaign {}".format(i)
            self.campaigns.append(Campaign(c_id, c_title))

    @staticmethod
    def all():
        from db.rpa.games import GAMES
        games = []
        for id, g in enumerate(GAMES):
            games.append(GameSystem.get(id + 1))
        return games

    @staticmethod
    def get(id):
        from db.rpa.games import GAMES
        g = GAMES[id - 1]
        game = GameSystem(id, g["name"])
        game.version = g.get("version", "7.13")
        game.path = g.get("path", "db")
        game.website = g.get("website", "")
        return game
    
    def __repr__(self):
        return "{} ({})".format(self.name, self.version)
