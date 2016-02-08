# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:05:52 2016

@author: 3200404
"""
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import Vector2D
from soccersimulator import settings
from tools import *


def goal(MyState,p):   
     
 
    if MyState.distanceBalleG() == 1 :
   
     
      return MyState.degager(p)
   
    else:
  
      return MyState.positionG(p)
       
      
      
def scoreG(MyState,p):
   
        return MyState.marquer(p)