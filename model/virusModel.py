import numpy as np
import random as rand
from mesa.datacollection import DataCollector
from mesa import Model, Agent
from mesa.time import RandomActivation
from model.fileIO.readData import getContactMatrices
from model.fileIO.readData import getPop
from model.places import Places
from model.agents import BaseAgent, ChildAgent, AdultAgent, YoungAgent, OldAgent, findMeetingNum

CONTACTMATRIX = getContactMatrices()
POP = getPop()

class VirusModel(Model):

    def __init__(self):

        self.popN = sum(POP)
        self.schedule = RandomActivation(self)
        self.agents = createPopulation(self)
        self.places = Places(self)
        self.places.placeAgents()
        # Create agents
        # for i in range(self.popN):
        #     a = BaseAgent(i, self)
        #     self.schedule.add(a)

        # a = ChildAgent(1, self, CONTACTMATRIX)
        # b = YoungAgent(2, self, CONTACTMATRIX)
        # c = AdultAgent(3, self, CONTACTMATRIX)
        # d = OldAgent(4, self, CONTACTMATRIX)

        # self.agents.append(a)
        # self.agents.append(b)
        # self.agents.append(c)
        # self.agents.append(d)

        # self.places.placeAgents()    
        # self.schedule.add(a)
        # self.schedule.add(b)
        # self.schedule.add(c)
        # self.schedule.add(d)

        for agent in self.agents:
            self.schedule.add(agent)
            findMeetingNum(agent)

       
    def getAgents(self):
        return self.agents

    def step(self):
        self.schedule.step()
        print(gatherMeetings(self))

def gatherMeetings(virusModel):
    agentMeetings = [agent.numberOfPeopleMet for agent in virusModel.schedule.agents]
    x = sum  (agentMeetings)
    return x

def createPopulation(self):
    iD = 0
    agents = list()
    for i in range(POP[0]):#children
        newAgent = ChildAgent(iD,self,CONTACTMATRIX)
        agents.append(newAgent)
        iD+=1
    for i in range(POP[1]):#youngadults
        newAgent = YoungAgent(iD,self,CONTACTMATRIX)
        agents.append(newAgent)
        iD+=1
    for i in range(POP[2]):#adults
        newAgent = AdultAgent(iD,self,CONTACTMATRIX)
        agents.append(newAgent)
        iD+=1
    for i in range(POP[3]):#elderly
        newAgent = OldAgent(iD,self,CONTACTMATRIX)
        agents.append(newAgent)
        iD+=1
    
    rand.shuffle(agents)
    return agents
        
