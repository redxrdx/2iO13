# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:09:00 2016

@author: 3200404
"""

from soccersimulator import SoccerAction
from soccersimulator import Vector2D
from soccersimulator import settings





def miroirP(p): 
 return (settings.GAME_WIDTH -p.x,p.y)

def miroirV(v):
    return (-v.x , -v.y)

class PlayerDecorator :
    
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        
    def position_joueur(self):
        return self.state.player.position

    def position_balle(self):
        return self.state.ball.position
        
    def marquer(self,p):
        return SoccerAction(self.state.ball.position - p.position,Vector2D(settings.GAME_HEIGHT,0))
    
    def degager(self,p):
        return SoccerAction(self.state.ball.position - p.position,Vector2D(settings.GAME_HEIGHT,20))
        
    def positionG(self,p):
        return SoccerAction(Vector2D(settings.GAME_WIDTH-10,settings.GAME_HEIGHT/2)-p.position, Vector2D(-(settings.GAME_HEIGHT),0))
    
    def distanceAll(self):
        v = self.state.player(1,0).position 
        w = self.state.player(1,1).position
        return v.distance(w)
        
    def distanceAdv1(self):
        v = self.state.player(1,0).position 
        w = self.state.player(2,1).position
        return v.distance(w)
        
    def distanceBalle(self):
    

     for j in range(0,1) :
        for i in range(1,2):
          v = self.state.player(i,j).position 
          w = self.state.ball.position
          if v.distance(w) < 10 :
        
            return  self.state.player(i,j)
        i = i +1         
     j = j+1
     
     return 0
     
     
    def distanceBalleG(self,p):
         if self.state.ball.position.x - p.position.x <= 30 or self.state.ball.position.x - p.position.x >= -30 :
             return 1
             
             
         
         
    
      