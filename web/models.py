#! /usr/bin/env python
# -*- coding:utf-8 -*-

PLACES = ['Adara', 'Adena', 'Adrianne', 'Alarice', 'Alvita', 'Amara', 'Ambika', 'Antonia', 'Araceli', 'Balandria', 'Basha',
'Beryl', 'Bryn', 'Callia', 'Caryssa', 'Cassandra', 'Casondrah', 'Chatha', 'Ciara', 'Cynara', 'Cytheria', 'Dabria', 'Darcei',
'Deandra', 'Deirdre', 'Delores', 'Desdomna', 'Devi', 'Dominique', 'Drucilla', 'Duvessa', 'Ebony', 'Fantine', 'Fuscienne',
'Gabi', 'Gallia', 'Hanna', 'Hedda', 'Jerica', 'Jetta', 'Joby', 'Kacila', 'Kagami', 'Kala', 'Kallie', 'Keelia', 'Kerry',
'Kerry-Ann', 'Kimberly', 'Killian', 'Kory', 'Lilith', 'Lucretia', 'Lysha', 'Mercedes', 'Mia', 'Maura', 'Perdita', 'Quella',
'Riona', 'Safiya', 'Salina', 'Severin', 'Sidonia', 'Sirena', 'Solita', 'Tempest', 'Thea', 'Treva', 'Trista', 'Vala', 'Winta']


import models.rpa


class PlayerCharacter:
    def __init__(self, id=0, name="Character"):
        self.id = id
        self.name = name
        self.attributes = "10, 10, 10, 10, 10, 10"
        self.HP = 8
        self.AC = 10
        self.saving_throw = "10, 10, 10"
        self.hands = ["+12", "-"]
        self.level = "2(1000xp)"

    def prev(self):
        if self.id > 1:
            return self.id - 2
        else:
            return 0

    def next(self):
        if self.id < 6:
            return self.id
        else:
            return 5

    def link(self):
        from flask.helpers import url_for
        return url_for("charsheet", char_id=self.id)


class RPG:
    def __init__(self, gs=None):
        self.gs = gs
        if type(self.gs) is not models.rpa.GameSystem:
            self.gs = models.rpa.GameSystem()

        self.id = self.gs.id
        self.name = self.gs.name
        self.version = self.gs.version
        self.path = self.gs.path
        self.website = self.gs.website

    def link(self):
        from flask.helpers import url_for
        return url_for("select_rpg", rpg_id=self.id)


pc = [
    PlayerCharacter(1, "Char1"),
    PlayerCharacter(2, "Char2"),
    PlayerCharacter(3, "Char3"),
    PlayerCharacter(4, "Char4"),
    PlayerCharacter(5, "Char5"),
    PlayerCharacter(6, "Char6"),
    ]


games = []
for g in models.rpa.games:
    games.append(RPG(g))
