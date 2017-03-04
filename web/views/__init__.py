#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import g, render_template, redirect, session
from flask.helpers import url_for
from web import app
from web.models import pc, current_rpg


# from web.views.char import character, new_character, edit_character
# from web.views.fraction import fraction, new_fraction, edit_fraction
from web.views.game_system import *
from web.views.campaign import *


@app.route("/session/add")
def session_add():
    return redirect(url_for("char_list"))


@app.route("/session/del")
def session_del():
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


@app.route("/name")
def list_names(country=""):
    return render_template("names.html")


@app.route("/name/world/<country>")
def random_name(country=""):
    names = []
    from models.markov import MCName
    from models.markov import MCRussianName
    from models import get_RussianName
    for i in range(100):
        names.append(MCName().New())
    names.append("---")
    for i in range(100):
        names.append(MCName(3).New())
    names.append("---")
    import random
    for i in range(100):
        if random.randrange(0, 2) > 0:
            c = False
        else:
            c = True
        names.append(get_RussianName(c))
    names.append("---")
    for i in range(100):
        names.append(MCRussianName().NewFull())
    names.append("---")
    for i in range(100):
        names.append(MCRussianName(3).NewFull())

    if country == "fiction":
        return render_template("names-fiction.html", names=names)
    elif country == "real":
        return render_template("names-real.html", names=names)
    elif country == "place":
        return render_template("names-place.html", names=names)
    elif country == "culture":
        return render_template("names-culture.html", names=names)
    elif country == "other":
        return render_template("names-other.html", names=names)
    elif country == "desc":
        return render_template("names-desc.html", names=names)
    elif country == "generator":
        return render_template("names-gen.html", names=[])
    return render_template("names.html", names=names)
