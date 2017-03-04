#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CampaignForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])