#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import app
from flask import g, render_template, redirect
from flask.helpers import url_for


# from web.views.char import character, new_character, edit_character
# from web.views.fraction import fraction, new_fraction, edit_fraction


wilderness1 = [
    {"id": 0, "title": "Пустынная", "chance": 5},
    {"id": 1, "title": "Дикая", "chance": 8},
    {"id": 2, "title": "Обитаемая", "chance": 10},
    {"id": 3, "title": "Густонаселенная", "chance": 12},
]

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
        return url_for("charsheet", char_id=self.id)


class RPG:
    def __init__(self, id=0, name="RPG"):
        self.id = id
        self.name = name
        

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


@app.route("/")
def index():
    return redirect(url_for("rpg_list"))


@app.route("/char")
def char_list():
    global pc
    g.pc = pc
    selected = pc[0]
    return redirect(url_for("charsheet", char_id=selected.id))


@app.route("/char/<int:char_id>")
def charsheet(char_id):
    if char_id <= 0:
        return redirect(url_for("char_list"))

    global pc
    g.pc = pc
    g.selected = pc[char_id - 1]
    return render_template("char.html")


@app.route("/rpg")
def rpg_list():
    global games
    return render_template("rpg.html", games=games)


@app.route("/rpg/<int:rpg_id>")
def select_rpg(rpg_id):
    if rpg_id <= 0:
        return redirect(url_for("rpg_list"))

    global games
    rpg = games[rpg_id - 1]
    return redirect(url_for("char_list"))