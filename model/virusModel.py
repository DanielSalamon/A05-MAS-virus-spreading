import numpy as np
import random as rand
from mesa import Agent, Model
from mesa.time import RandomActivation
from model.fileIO.readData import getContactMatrices
from model.places import Places
from model.agents import BaseAgent, ChildAgent, AdultAgent, YoungAgent, OldAgent

CONTACTMATRIX = getContactMatrices()

class VirusModel(Model):

    def __init__(self, popN):

        self.popN = popN
        self.schedule = RandomActivation(self)
        self.agents = list()
        self.places = Places(self)
        # Create agents
        # for i in range(self.popN):
        #     a = BaseAgent(i, self)
        #     self.schedule.add(a)

        a = ChildAgent(1, self, CONTACTMATRIX)
        b = YoungAgent(2, self, CONTACTMATRIX)
        c = AdultAgent(3, self, CONTACTMATRIX)
        d = OldAgent(4, self, CONTACTMATRIX)

        self.agents.append(a)
        self.agents.append(b)
        self.agents.append(c)
        self.agents.append(d)

        self.places.placeAgents()
        
        a.house.display()
        b.house.display()
        c.house.display()
        d.house.display()
        
        self.schedule.add(a)
       
    def getAgents(self):
        return self.agents

    def step(self):
        self.schedule.step()
        #print(self.status)

a = getContactMatrices()
# t = transmission rate
# Cij = contatcts of agegroup j made by agegroup i
# k = 1-exp(-1\incubation period) -> daily probability of individual becoming infectious
