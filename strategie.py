# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:23:06 2016

@author: 3200404
"""


from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import Vector2D
from soccersimulator import settings
from tools import MyState



class Goal(BaseStrategy):
  
  def __init__(self):
      BaseStrategy.__init__(self, "Random")
 
  def compute_strategy(self,state,id_team,id_player):
      p = state.player_state(id_team,id_player)       
      return MyState(state,id_team,id_player).goal(p)
  
        


class Goal2(BaseStrategy):
  
  def __init__(self):
      BaseStrategy.__init__(self, "Random")
 
  def compute_strategy(self,state,id_team,id_player):
   p = state.player_state(id_team,id_player) 
  
   if (state.ball.position.x <= 20 and state.ball.position.y > 35 and state.ball.position.y < 55):
        return SoccerAction((state.ball.position - p.position),Vector2D(settings.GAME_HEIGHT,0))
   else :
        return SoccerAction(Vector2D(10,settings.GAME_HEIGHT/2)-p.position, Vector2D(settings.GAME_HEIGHT,0))
   
   


class Defence(BaseStrategy):
   def __init__(self):
      BaseStrategy.__init__(self, "Random")
   def compute_strategy(self,state,id_team,id_player):
     p = state.player_state(id_team,id_player) 
     
     if (MyState(state,id_team,id_player).distanceAll() < 10) :
         return SoccerAction(Vector2D(settings.GAME_WIDTH -70,state.ball.position.y)-p.position, Vector2D(0,0))
   
     if (MyState(state,id_team,id_player).position_balle()> 75):
         return SoccerAction((state.ball.position - p.position),Vector2D(-(settings.GAME_HEIGHT),0))
  
     else :
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
       
     #  if (MyState(state,id_team,id_player).distanceAdv1() < 5 and MyState(state,id_team,id_player).distanceBalle() < 5) : 
      #   return SoccerAction(Vector2D(settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)-p.position, Vector2D(0,0))
         
       if (MyState(state,id_team,id_player).distanceAdv1() > 10 and MyState(state,id_team,id_player).distanceBalle() < 10) :
         return MyState(state,id_team,id_player).marquer(p)   
       else:
          return SoccerAction(Vector2D(settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)-p.position, Vector2D(0,0))
       
       
       
class Score2(BaseStrategy):
     def __init__(self):
      BaseStrategy.__init__(self, "Random")
     def compute_strategy(self,state,id_team,id_player):
       p = state.player_state(id_team,id_player)   
       return SoccerAction(state.ball.position - p.position,Vector2D(-(settings.GAME_HEIGHT),0))
