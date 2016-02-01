# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:29:33 2016

@author: 3200404
"""

 
from strategie import Goal
from strategie import Score
from strategie import Score2
from strategie import Goal2
from soccersimulator import SoccerTeam,Player

team1 = SoccerTeam("team1",[Player("CR7",Score()),Player("ramos",Goal2())])
team2 = SoccerTeam("team2",[Player("pique",Goal()),Player("MESSI",Score2())])
