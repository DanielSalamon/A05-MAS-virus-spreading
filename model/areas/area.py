from numpy import size
from model.agents import ChildAgent, OldAgent, AdultAgent, YoungAgent

class Area():
    def __init__(self,idNum = 0):
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
        self.members = [self.children, self.youngAdults, self.adults, self.elderly]

    def addMember(self, agent):
        if not self.full:
            sortAgent(self,agent)
            self.memNum += 1
            if self.capacity == self.memNum:
                self.full = True
    
    def display(self):
        print('num of Children: '+str(size(self.children)))
        print('num of YoungAdults: '+str(size(self.youngAdults)))
        print('num of Adults: '+str(size(self.adults)))
        print('num of Elderly: '+str(size(self.elderly)))

    def meet(self, agent1, agent2):

        pass

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

