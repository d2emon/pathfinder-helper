#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, session
from flask.helpers import url_for
from web import app
from web.models import current_rpg
from models.rpa import games


@app.route("/")
def index():
    return redirect(url_for("rpg_list"))


@app.route("/rpg")
def rpg_list():
    return render_template("rpg.html", games=games, selected=current_rpg())


@app.route("/rpg/add")
def rpg_add():
    return redirect(url_for("char_list"))


@app.route("/rpg/del")
def rpg_del():
    return redirect(url_for("char_list"))


@app.route("/rpg/<int:rpg_id>")
def select_rpg(rpg_id):
    session["rpg"] = rpg_id
    if rpg_id <= 0:
        return redirect(url_for("rpg_list"))

    rpg = current_rpg()
    return redirect(url_for("campaign_list"))