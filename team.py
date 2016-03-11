# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:29:33 2016

@author: 3200404
"""

 

from strategie import *
from soccersimulator import SoccerTeam,Player
from decisiontree import DTreeStrategy , gen_features
import cPickle
import os

fn = os.path.join(os.path.dirname(os.path.realpath(__file__)), "millieu.pkl")
fn2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "attaque.pkl")
fn3 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "defense.pkl")


team2j = SoccerTeam("k2",[Player("serge",defenseG),Player("ramos",attaqueG)])
team2j2 = SoccerTeam("team2",[Player("pique",attaqueG),Player("masherano",defenseG)])
teamREAL = SoccerTeam("team1",[Player("CR7",pointe),Player("ramos",defenseG),Player("marcelo",millieu),Player("navas",goalG)])
teamPSG4 = SoccerTeam("team1",[Player("trapp",goalG),Player("silva",central),Player("aurier",defenseG),Player("zlatan",attaqueG)])
team1j = SoccerTeam("k1",[Player("serge",joueur1)])
team12j = SoccerTeam("team1",[Player("ert",attaqueG)])

teama4 = SoccerTeam("test",[Player("t",goalG),Player("s",defenseG),Player("a",millieu),Player("z",pointe)])

tree = cPickle.load(file("./mon_fichier.pkl"))
dic = {"goal":goalG,"attaquant":attaqueG,"defenseur":defenseG,"millieu":millieu,"defenseCentral":central,"conserver":conserver,"dribbler":dribbler,"tirer":tirer,"passer":passer,"finition":finition}
treeStrat = DTreeStrategy(tree,dic,gen_features)

millieuI = cPickle.load(file("./millieu.pkl"))
dic = {"goal":goalG,"attaquant":attaqueG,"defenseur":defenseG,"millieu":millieu,"defenseCentral":central,"conserver":conserver,"dribbler":dribbler,"tirer":tirer,"passer":passer,"finition":finition}
MStrat = DTreeStrategy(millieuI,dic,gen_features)

attaqueI = cPickle.load(file("./attaque.pkl"))
dic = {"goal":goalG,"attaquant":attaqueG,"defenseur":defenseG,"millieu":millieu,"defenseCentral":central,"conserver":conserver,"dribbler":dribbler,"tirer":tirer,"passer":passer,"finition":finition,"position":position}
AStrat = DTreeStrategy(attaqueI,dic,gen_features)

defenseI = cPickle.load(file("./defense.pkl"))
dic = {"goal":goalG,"attaquant":attaqueG,"defenseur":defenseG,"millieu":millieu,"defenseCentral":central,"conserver":conserver,"dribbler":dribbler,"tirer":tirer,"passer":passer,"finition":finition,"position":position,"dc":central}
DStrat = DTreeStrategy(defenseI,dic,gen_features)


teamIA = SoccerTeam("team1",[Player("ert",MStrat),Player("ramos",goalG),Player("t",AStrat),Player("s",DStrat)])