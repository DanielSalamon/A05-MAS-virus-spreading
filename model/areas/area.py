from numpy import size
from model.agents import ChildAgent, OldAgent, AdultAgent, YoungAgent

class Area():
    def __init__(self):
        self.capacity = 1
        self.memNum = 0
        self.full = False
        self.numberOfInfected = 0

        self.children = list()
        self.youngAdults = list()
        self.adults = list()
        self.elderly = list()

    def addMember(self, agent):
        if not self.full:
            sortAgent(self,agent)
            self.memNum += 1
            if self.capacity == self.memNum:
                self.full = True
        return not self.full
    
    def isFull(self):
        return self.full

    def display(self):
        print('num of Children: '+str(size(self.children)))
        print('num of YoungAdults: '+str(size(self.youngAdults)))
        print('num of Adults: '+str(size(self.adults)))
        print('num of Elderly: '+str(size(self.elderly)))

def sortAgent(self, agent):
        if isinstance(agent, ChildAgent):
            self.children.append(agent)
        if isinstance(agent, YoungAgent):
            self.youngAdults.append(agent)
        if isinstance(agent, AdultAgent):
            self.adults.append(agent)
        if isinstance(agent, OldAgent):
            self.elderly.append(agent)