from numpy import size
from model.agents import ChildAgent, OldAgent, AdultAgent, YoungAgent
import random as rand


class Area():
    def __init__(self):
        self.capacity = 1 # capacity of agents in one area
        self.memNum = 0 # current number of members
        self.full = False 
        self.numberOfInfected = 0
        self.areaType = ''

        self.children = list() # lists of members of certain type
        self.youngAdults = list()
        self.adults = list()
        self.elderly = list()
        self.members = [self.children, self.youngAdults, self.adults, self.elderly]

        self.attack_rate = 0.1 # estimation from paper "Estimation of Individual Probabilities of COVID-19 
        # Infection, Hospitalization, and Death From A County-level Contact of Unknown infection Status"


    def addMember(self, agent): #function to add member change full attribute if capacity reached
        if not self.full:
            sortAgent(self, agent)
            self.memNum += 1
            if self.capacity == self.memNum:
                self.full = True

    def meet(self, agent1, agent2):# meeting of two agents in certain area
        if agent1.status == "susceptible" and agent2.status == "infected":
            chance = self.infectionChance(agent1,agent2) 
            if (chance > rand.random()):
                agent1.status = "exposed"

        # elif agent1.status == "infected" and agent2.status == "susceptible": 
        #     if (self.attack_rate > rand.random()):
        #         agent2.status = "exposed"

    def infectionChance(self, agent1, agent2):
        maskReceiveProb = 1 #TODO find the mask transmssion and reception probs
        maskTransmitProb = 1
        chance = self.attack_rate

        if agent1.mask and agent2.mask:
            chance = maskTransmitProb * maskTransmitProb
        elif agent1.mask:
            chance = maskReceiveProb
        elif agent2.mask:
            chance = maskTransmitProb
        
        return chance


    def removeAgent(self, agent): #remove agent from corresponding list
        if isinstance(agent, ChildAgent):
            self.children.remove(agent)
            self.members[0] = self.children
        if isinstance(agent, YoungAgent):
            self.youngAdults.remove(agent)
            self.members[1] = self.youngAdults
        if isinstance(agent, AdultAgent):
            self.adults.remove(agent)
            self.members[2] = self.adults
        if isinstance(agent, OldAgent):
            self.elderly.remove(agent)
            self.members[3] = self.elderly


def sortAgent(self, agent): #add agent to corresponding list
    if isinstance(agent, ChildAgent):
        self.children.append(agent)
        self.members[0] = self.children
    if isinstance(agent, YoungAgent):
        self.youngAdults.append(agent)
        self.members[1] = self.youngAdults
    if isinstance(agent, AdultAgent):
        self.adults.append(agent)
        self.members[2] = self.adults
    if isinstance(agent, OldAgent):
        self.elderly.append(agent)
        self.members[3] = self.elderly


