# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:05:54 2016

@author: 3200404
"""

import soccersimulator,soccersimulator.settings
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Player, SoccerTournament, Vector2D
from soccersimulator import settings

  
    
class Goal(BaseStrategy):
   def __init__(self):
      BaseStrategy.__init__(self, "Random")
   def compute_strategy(self,state,id_team,id_player):
     p = state.player_state(id_team,id_player) 
     if (state.ball.position.x > 75):
        print ("ss scale", Vector2D((state.ball.position.x - p.position.x),(state.ball.position.y - p.position.y)))
        print ("av scale", Vector2D((state.ball.position.x - p.position.x),(state.ball.position.y - p.position.y)).scale(1.))
        return SoccerAction(Vector2D((state.ball.position.x - p.position.x),(state.ball.position.y - p.position.y))*0.2,Vector2D(-(settings.GAME_HEIGHT),0))
     else:
          return SoccerAction(Vector2D(settings.GAME_WIDTH-10,settings.GAME_HEIGHT/2)-p.position, Vector2D(0,0))
       
        
class Goal2(BaseStrategy):
   def __init__(self):
      BaseStrategy.__init__(self, "Random")
   def compute_strategy(self,state,id_team,id_player):
     p = state.player_state(id_team,id_player) 
     if (state.ball.position.x <= 20 and state.ball.position.y > 35 and state.ball.position.y < 55):
        return SoccerAction((state.ball.position - p.position),Vector2D(settings.GAME_HEIGHT,0))
     else :
        return SoccerAction(Vector2D(10,settings.GAME_HEIGHT/2)-p.position, Vector2D(0,0))
   
   
class Defence(BaseStrategy):
   def __init__(self):
      BaseStrategy.__init__(self, "Random")
   def compute_strategy(self,state,id_team,id_player):
     p = state.player_state(id_team,id_player) 
     if (state.ball.position.x > 75):
        return SoccerAction((state.ball.position - p.position),Vector2D(-(settings.GAME_HEIGHT),0))
     else:
        return SoccerAction(Vector2D(settings.GAME_WIDTH -70,state.ball.position.y)-p.position, Vector2D(0,0))
        
class Defence2(BaseStrategy):
   def __init__(self):
      BaseStrategy.__init__(self, "Random")
   def compute_strategy(self,state,id_team,id_player):
     p = state.player_state(id_team,id_player) 
     if (state.ball.position.x < 75):
        return SoccerAction((state.ball.position - p.position),Vector2D((settings.GAME_HEIGHT),0))
     else:
        return SoccerAction(Vector2D(70,state.ball.position.y)-p.position, Vector2D(0,0))        
   
class Score(BaseStrategy):
     def __init__(self):
      BaseStrategy.__init__(self, "Random")
     def compute_strategy(self,state,id_team,id_player):
       p = state.player_state(id_team,id_player)   
       return SoccerAction(state.ball.position - p.position,Vector2D(settings.GAME_HEIGHT,0))
       
       
       
class Score2(BaseStrategy):
     def __init__(self):
      BaseStrategy.__init__(self, "Random")
     def compute_strategy(self,state,id_team,id_player):
       p = state.player_state(id_team,id_player)   
       return SoccerAction(state.ball.position - p.position,Vector2D(-(settings.GAME_HEIGHT),0))

    

team1 = SoccerTeam("team1",[Player("CR7",Score()),Player("ramos",Defence2())])
team2 = SoccerTeam("team2",[Player("pique",Goal()),Player("MESSI",Defence())])
match = SoccerMatch(team1, team2)

soccersimulator.show(match)