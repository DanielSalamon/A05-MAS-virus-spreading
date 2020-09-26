from mesa import Agent, Model
from mesa.time import RandomActivation
import numpy as np
import random as rand
from random import randint
from agents.baseAgent import *
from readData import getContactMatrices

CONTACTMATRIX = getContactMatrices()

class VirusModel(Model):

    def __init__(self, popN):

        self.popN = popN
        self.schedule = RandomActivation(self)
        self.agents = list()
        self.houses
        # Create agents
        # for i in range(self.popN):
        #     a = BaseAgent(i, self)
        #     self.schedule.add(a)

        a = BaseAgent(1, self, CONTACTMATRIX)
        self.schedule.add(a)
       


    def step(self):
        self.schedule.step()
        #print(self.status)

def assignAgents(self):
   # for agent in self.agents:
    pass

a = getContactMatrices()
# t = transmission rate
# Cij = contatcts of agegroup j made by agegroup i
# k = 1-exp(-1\incubation period) -> daily probability of individual becoming infectious
