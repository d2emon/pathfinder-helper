#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, session
from flask.helpers import url_for

from web import app
from web.models import current_rpg

from models.rpa import Campaign
from db import db_session

@app.route("/campaign")
def campaign_list():
    # rpg = current_rpg()
    rpg = session.get("rpg", None)
    if rpg is None:
        return redirect(url_for('rpg_list'))

    campaigns = Campaign.query.filter(Campaign.gs_id==rpg.id).all() 
    print(campaigns)
    return render_template("campaigns.html", campaigns=campaigns)


@app.route("/campaign/add")
def campaign_add():
    return redirect(url_for("char_list"))


@app.route("/campaign/del/<int:campaign_id>")
def campaign_del(campaign_id):
    campaign = Campaign.query.get(campaign_id) 
    db_session.delete(campaign)
    db_session.commit()
        
    return redirect(url_for("campaign_list"))


@app.route("/campaign/<int:campaign_id>")
def session_list(campaign_id):
    # rpg = current_rpg()
    rpg = session.get("rpg", None)
    if rpg is None:
        return redirect(url_for('rpg_list'))

    campaign = rpg.getCampaign(campaign_id)
    print(campaign)
    session["campaign"] = campaign
    
    return redirect(url_for("char_list"))
    # return render_template("campaigns.html", campaigns=campaigns, selected=games[rpg_id])