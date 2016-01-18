# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:05:54 2016

@author: 3200404
"""

import soccersimulator,soccersimulator.settings
from soccersimulator import AbstractStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Player, SoccerTournament, Vector2D
from soccersimulator import settings

    
    
class RandomStrategy(AbstractStrategy):
   def __init__(self):
      AbstractStrategy.__init__(self, "Random")
   def compute_strategy(self,state,id_team,id_player):
      
       return SoccerAction(Vector2D.create_random(-2,2),Vector2D.create_random())
   

class Score(AbstractStrategy):
     def __init__(self):
      AbstractStrategy.__init__(self, "Random")
     def compute_strategy(self,state,id_team,id_player):
       p = state.player_state(id_team,id_player)   
       return SoccerAction(state.ball.position - p.position,Vector2D(settings.GAME_HEIGHT,0))

team1 = SoccerTeam("team1",[Player("CR7",Score())])
team2 = SoccerTeam("team2",[Player("PIQUE",RandomStrategy())])
match = SoccerMatch(team1, team2)

soccersimulator.show(match)