# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:29:33 2016

@author: 3200404
"""

 

from strategie import *
from soccersimulator import SoccerTeam,Player
from decisiontree import DTreeStrategy , gen_features
import cPickle

team2j = SoccerTeam("team1",[Player("serge",passer),Player("ramos",attaqueG)])
team2j2 = SoccerTeam("team2",[Player("pique",defenseG),Player("masherano",central)])
teamREAL = SoccerTeam("team1",[Player("CR7",pointe),Player("ramos",defenseG),Player("marcelo",lateralG),Player("navas",goalG)])
teamPSG4 = SoccerTeam("team1",[Player("trapp",goalG),Player("silva",central),Player("aurier",defenseG),Player("zlatan",attaqueG)])
team1j = SoccerTeam("team1",[Player("serge",keytest)])
team12j = SoccerTeam("team1",[Player("ert",defenseG)])

teama4 = SoccerTeam("test",[Player("t",central),Player("s",defenseG),Player("a",keytest),Player("z",pointe)])

tree = cPickle.load(file("./mon_fichier.pkl"))
dic = {"goal":goal,"attaquant":scoreG,"defenseur":defence,"millieu":millieu,"defenseCentral":Dcentral,"conserver":conserver,"dribbler":dribbler,"tirer":tirer,"passer":passer}
treeStrat = DTreeStrategy(tree,dic,gen_features)

teamIA = SoccerTeam("team1",[Player("ert",treeStrat),Player("ramos",goalG)])