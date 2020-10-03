from numpy import size
from model.agents import ChildAgent, OldAgent, AdultAgent, YoungAgent
import random as rand


class Area():
    def __init__(self, idNum=0):
        self.idNum = idNum
        self.capacity = 1
        self.memNum = 0
        self.full = False
        self.numberOfInfected = 0
        self.areaType = ''

        self.children = list()
        self.youngAdults = list()
        self.adults = list()
        self.elderly = list()
        self.members = [self.children,
                        self.youngAdults, self.adults, self.elderly]

    def addMember(self, agent):
        if not self.full:
            sortAgent(self, agent)
            self.memNum += 1
            if self.capacity == self.memNum:
                self.full = True

    def meet(self, agent1, agent2):
        
        if agent1.status == "susceptible" and agent2.status == "infected": 
            prob_of_infection = agent1.prob_infected * agent2.prob_infect
            if (prob_of_infection > rand.random()):
                agent1.status = "exposed"

        elif agent1.status == "infected" and agent2.status == "susceptible": 
            prob_of_infection = agent1.prob_infect * agent2.prob_infected
            if (prob_of_infection > rand.random()):
                agent2.status = "exposed"

    def removeAgent(self, agent):
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


def sortAgent(self, agent):
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


