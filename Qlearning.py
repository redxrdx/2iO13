# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:42:24 2016

@author: 3200404
"""

from soccersimulator import settings, SoccerAction,Vector2D,DecisionTreeClassifier, KeyboardStrategy, BaseStrategy
from soccersimulator import export_graphviz
import cPickle
import sys
from Tools import *
from collections import defaultdict
from Player_strat import *


#######################VALEURS GLOBAL##############
alpha = 0.1
gamma = 0.9
epsilon = 0.1

#################################################

class PlayerIA :
    def __init__(self , state , id_team , id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player 
        self.suivre =0
        self.tirer =0
        self.avancer = 0
      
        
        
    
def discretisation (state,id_team,id_player):
 
     Mystate = PlayerStateDecorator(state,id_team,id_player)
     Liste = []
     
     
       #Distance allie  
     if Mystate.distance_alliexy(0,10): 
        pa = 0
     elif Mystate.distance_alliexy(10,20):
        pa = 1
     elif Mystate.distance_alliexy(20,30):
        pa = 2
     elif Mystate.distance_alliexy(30,40):
        pa = 3
     else :
        pa = 4
        
     liste.append(pa)
        
            # Distance adversaire    
     if Mystate.distance_adversairexy(0,10): 
        pad = 0
     elif Mystate.distance_adversairexy(10,20):
        pad = 1
     elif Mystate.distance_adversairexy(20,30):
        pad = 2
     elif Mystate.distance_adversairexy(30,40):
        pad = 3
     else :
        pad = 4
        
     liste.append(pad)   
        #distance de mes buts
        
     if MyState.distance_Mesbuts(0,10):
           mb = 0 
     elif MyState.distance_Mesbuts(10,20):
            mb = 1
     elif MyState.distance_Mesbuts(20,30):
            mb = 3
     elif MyState.distance_Mesbuts(30,50):
            mb = 4
     else:
            mb = 5
       
       
     liste.append(mb)
               #distance buts adverses
        
     if MyState.distance_butsadv(0,10):
           mbd = 0 
     elif MyState.distance_butsadv(10,20):
            mbd = 1
     elif MyState.distance_butsadv(20,30):
            mbd = 3
     elif MyState.distance_butsadv(30,50):
            mbd = 4
     else:
            mbd = 5
          
          
     liste.append(mbd)
            
            #distance de la balle
        
        
     if MyState.distance_ballexy(0,10):
            db = 0
     elif MyState.distance_ballexy(10,20):
            db = 1
     elif MyState.distance_ballexy(20,30):
            db = 2
     elif MyState.distance_ballexy(30,40):
            db = 3
     elif MyState.distance_ballexy(40,50):
            db = 4   
     else : 
            db = 5
            
        # si le joueur possede la balle 
     if (db == 0):
         if MyState.possede_balle():
               db = 9
         else : 
                db = 0
            
            
     liste.append(db)
        
     return tuple(Liste)
     
     
     
     #def Q(state,id_team,id_player):
#        
#      dicoaction = {"conserver":conserver,"dribbler":dribbler,"tirer":tirer,finition":finition"}
#                 
#      S = discretisation(state,id_team,id_player)
#                
#                      
#      senario{S : dicoation}
#      return senario 
#
#
#Q =  dict()
#Q[s]=defaultdict(float)
#Q[s][a] 



#def Monte_carlo(Q= None, scenario = [(state,action)...,(state,action)]):
#    
#       R = recompense(senario[-1][0])      
#      #  if Q is None:
#       #     Q = dict()
#     
#        for (s,a) in senario[-2::-1]:
#            if s not in Q:
#                # descritisation 
#                s = discretisation(self.state,self.id_team,self.id_player)
#                self.Q[s] = defaultdict(float)
#                self.Q[s][a] = 0
#       
#        for (s,a) in senario[-2::-1]:
#            self.Q[s][a] = self.Q[s][a] + alpha*(R-self.Q[s][a])
#            R = gamma * R +recompense(s)
#        