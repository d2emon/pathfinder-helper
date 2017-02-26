#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import app
from web.models import games, pc
from flask import g, render_template, redirect
from flask.helpers import url_for


# from web.views.char import character, new_character, edit_character
# from web.views.fraction import fraction, new_fraction, edit_fraction


@app.route("/")
def index():
    return redirect(url_for("rpg_list"))


@app.route("/rpg")
def rpg_list():
    rpg_id = 0
    return render_template("rpg.html", games=games, selected=games[rpg_id])


@app.route("/rpg/add")
def rpg_add():
    return redirect(url_for("char_list"))


@app.route("/rpg/del")
def rpg_del():
    return redirect(url_for("char_list"))


@app.route("/rpg/<int:rpg_id>")
def select_rpg(rpg_id):
    if rpg_id <= 0:
        return redirect(url_for("rpg_list"))

    rpg = games[rpg_id - 1]
    return redirect(url_for("char_list"))


@app.route("/char")
def char_list():
    g.pc = pc
    selected = pc[0]
    return redirect(url_for("charsheet", char_id=selected.id))


@app.route("/char/add")
def char_add():
    return redirect(url_for("char_list"))


@app.route("/char/del")
def char_del():
    return redirect(url_for("char_list"))


@app.route("/char/<int:char_id>")
def charsheet(char_id):
    if char_id <= 0:
        return redirect(url_for("char_list"))

    g.pc = pc
    g.selected = pc[char_id - 1]
    return render_template("char.html")
