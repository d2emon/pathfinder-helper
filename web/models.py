#! /usr/bin/env python
# -*- coding:utf-8 -*-

PLACES = ['Adara', 'Adena', 'Adrianne', 'Alarice', 'Alvita', 'Amara', 'Ambika', 'Antonia', 'Araceli', 'Balandria', 'Basha',
'Beryl', 'Bryn', 'Callia', 'Caryssa', 'Cassandra', 'Casondrah', 'Chatha', 'Ciara', 'Cynara', 'Cytheria', 'Dabria', 'Darcei',
'Deandra', 'Deirdre', 'Delores', 'Desdomna', 'Devi', 'Dominique', 'Drucilla', 'Duvessa', 'Ebony', 'Fantine', 'Fuscienne',
'Gabi', 'Gallia', 'Hanna', 'Hedda', 'Jerica', 'Jetta', 'Joby', 'Kacila', 'Kagami', 'Kala', 'Kallie', 'Keelia', 'Kerry',
'Kerry-Ann', 'Kimberly', 'Killian', 'Kory', 'Lilith', 'Lucretia', 'Lysha', 'Mercedes', 'Mia', 'Maura', 'Perdita', 'Quella',
'Riona', 'Safiya', 'Salina', 'Severin', 'Sidonia', 'Sirena', 'Solita', 'Tempest', 'Thea', 'Treva', 'Trista', 'Vala', 'Winta']

NAMES = [
  "Лев",
  "Данила",
  "Борис",
  "Юрий",
  "Спиридон",
  "Валентин",
  "Лука",
  "Самбор",
  "Владислав",
  "Станислав",
  "Ярослав",
  "Ростислав",
  "Валерий",
  "Василий",
  "Виталий",
  "Дмитрий",
  "Филипп",
  "Павел",
  "Кирилл",
  "Владимир",
  "Артем",
  "Викентий",
  "Никодим",
  "Валерьян",
  "Милослав",
  "Агафон",
  "Велимир",
  "Иван",
  "Герман",
  "Вячеслав",
  "Святослав",
  "Андрей",
  "Зиновий",
  "Антон",
  "Яромир",
  "Анатолий",
  "Дамир",
  "Богдан",
  "Аркадий",
  "Лукьян",
  "Исаак",
  "Август",
  "Самуил",
  "Никифор",
  "Тарас",
  "Доминик",
  "Илья",
  "Братислав",
  "Петр",
  "Абрам",
  "Иннокентий",
  "Михаил",
  "Егор",
  "Федор",
  "Вениамин",
  "Всеволод",
  "Олег",
  "Ян",
  "Георгий",
  "Милан",
  "Еремей",
  "Карл",
  "Добромил",
  "Мудозвон",
  "Мстислав",
  "Прохор",
  "Денис",
  "Демьян",
  "Макар",
  "Глеб",
  "Александр",
  "Вадим",
  "Яков",
  "Виктор",
  "Алексей",
  "Игорь",
]

import random


class MCDict:
    def __init__(self):
        self.d = {}

    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)

    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]

    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)  


class MCName:
    """
    A name from a Markov chain
    """
    def __init__(self, chainlen = 2):
        """
        Building the dictionary
        """
        # if chainlen > 10 or chainlen < 1:
            # print "Chain length must be between 1 and 10, inclusive"
            # sys.exit(0)
    
        self.mcd = MCDict()
        oldnames = []
        self.chainlen = chainlen
    
        for l in NAMES:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")
    
    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()  


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
        from flask.helpers import url_for
        return url_for("charsheet", char_id=self.id)


class RPG:
    def __init__(self, id=0, name="RPG"):
        self.id = id
        self.name = name
        self.version = "7.13"
        self.path = self.name
        self.website = ""
        
    def link(self):
        from flask.helpers import url_for
        return url_for("select_rpg", rpg_id=self.id)
        

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
