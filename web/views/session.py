#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, session, flash
from flask.helpers import url_for

from web import app
from web.forms import CampaignForm

from models.rpa import GameSession
from db import db_session


@app.route("/session")
def session_list():
    # rpg = current_rpg()
    campaign = session.get("campaign", None)
    if campaign is None:
        return redirect(url_for('campaign_list'))

    sessions = GameSession.query.filter(GameSession.campaign_id==campaign.id).all() 
    return render_template("session/list.html", sessions=sessions)


@app.route("/session/add", methods=('GET', 'POST'))
@app.route("/session/edit/<int:session_id>", methods=('GET', 'POST'))
def session_edit(session_id=0):
    if campaign_id > 0:
        campaign = Campaign.query.get(campaign_id)
    else:
        campaign = Campaign()
        campaign.gs_id = session["rpg"].id

    form = CampaignForm()
    if form.validate_on_submit():
        campaign.title = form.title.data
        db_session.add(campaign)
        db_session.commit()
        
        flash("Кампания {} успешно добавлена".format(campaign))
        return redirect(url_for('session_list'))
    form.title.data = campaign.title
    return render_template("session/edit.html", form=form, campaign_id=campaign.id)


@app.route("/session/del/<int:session_id>")
def session_del(session_id):
    campaign = Campaign.query.get(campaign_id) 
    flash("Кампания {} успешно удалена".format(campaign))
    db_session.delete(campaign)
    db_session.commit()
        
    return redirect(url_for("session_list"))


@app.route("/session/<int:session_id>")
def session_show(session_id):
    # rpg = current_rpg()
    rpg = session.get("rpg", None)
    if rpg is None:
        return redirect(url_for('campaign_list'))

    campaign = Campaign.query.get(campaign_id) 
    session["campaign"] = campaign
    
    return redirect(url_for("char_list"))
    # return render_template("campaigns.html", campaigns=campaigns, selected=games[rpg_id])