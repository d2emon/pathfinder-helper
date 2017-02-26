#! /usr/bin/env python
# -*- coding:utf-8 -*-

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
    def __init__(self, id=0, name="RPG"):
        self.id = id
        self.name = name
        self.version = "7.13"
        self.path = self.name
        self.website = ""
        
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


games = [
    RPG(1, "ADnD 2nd edition"),   
    RPG(2, "ADnD 3rd edition"),   
    RPG(3, "ADnD 3.5 edition"),   
    RPG(4, "ADnD-Wyrms"),   
    ]
