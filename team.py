# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:29:33 2016

@author: 3200404
"""

 
from strategie import Goal
from strategie import Defence
from strategie import ScoreG
from strategie import GoalG
from soccersimulator import SoccerTeam,Player

team1 = SoccerTeam("team1",[Player("CR7",ScoreG()),Player("ramos",GoalG())])
team2 = SoccerTeam("team2",[Player("pique",Goal()),Player("MESSI",ScoreG())])
