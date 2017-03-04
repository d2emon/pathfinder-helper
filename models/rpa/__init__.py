#! /usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base


class GameSystem(Base):
    __tablename__ = 'game_system'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    version = Column(String(16))
    website = Column(String(255))
    campaigns = relationship("Campaign")
    
    def __repr__(self):
        return "{} ({})".format(self.name, self.version)


class Campaign(Base):
    __tablename__ = 'campaign'
    id = Column(Integer, primary_key=True)
    gs_id = Column(Integer, ForeignKey('game_system.id'))
    title = Column(String(32))
    
    def __repr__(self):
        return self.title


class CampaignOld:
    def __init__(self, id=0, title="Campaign"):
        self.id = id
        self.title = title


class GameSystemOld():
    def __init__(self, id=0, name="RPG"):
        self.id = id
        self.name = name
        self.version = "7.13"
        self.path = "db"
        self.website = ""
        # self.campaigns = self.getCampaigns()

    @staticmethod
    def all():
        from db.rpa.games import GAMES
        games = []
        for id, g in enumerate(GAMES):
            games.append(GameSystem.get(id + 1))
        return games

    @staticmethod
    def get(id):
        from db.rpa.games import GAMES
        g = GAMES[id - 1]
        game = GameSystem(id, g["name"])
        game.version = g.get("version", "7.13")
        game.path = g.get("path", "db")
        game.website = g.get("website", "")
        return game
    
    def getCampaigns(self):
        filename = self.path + "/campaigns.txt"
        print("filename", self.name, filename)
        
        import os
        if not os.path.exists(filename):
            return []

        campaigns = []
        with open(filename, "r") as campaigns_file:
            for c_id, c_title in enumerate(campaigns_file.readlines()):
                campaigns.append(Campaign(c_id + 1, c_title))
        return campaigns

    def getCampaign(self, id=0):
        campaigns = self.getCampaigns()
        return campaigns[id - 1]