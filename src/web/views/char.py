#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import g, render_template, redirect, session
from flask.helpers import url_for
from web import app
from web.models import pc


@app.route("/char")
def char_list():
    g.pc = pc
    g.selected = pc[0]
    return redirect(url_for("charsheet", char_id=g.selected.id))


@app.route("/char/add")
def char_add():
    g.pc = pc
    g.selected = pc[0]
    return render_template("char/add.html")


@app.route("/char/del")
def char_del():
    return redirect(url_for("char_list"))


@app.route("/char/<int:char_id>")
def charsheet(char_id):
    print(session["session"])
    if char_id <= 0:
        return redirect(url_for("char_list"))

    g.pc = pc
    g.selected = pc[char_id - 1]
    return render_template("char/view.html")
