#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import app
from flask import render_template

# from web.views.char import character, new_character, edit_character
# from web.views.fraction import fraction, new_fraction, edit_fraction


wilderness1 = [
    {"id": 0, "title": "Пустынная", "chance": 5},
    {"id": 1, "title": "Дикая", "chance": 8},
    {"id": 2, "title": "Обитаемая", "chance": 10},
    {"id": 3, "title": "Густонаселенная", "chance": 12},
]


@app.route("/")
def index():
    return render_template("index.html")