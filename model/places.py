from model.areas import Home, Other, School, Work
from model.agents.baseAgent import *

class Places():

    def __init__(self, virusModel):

        self.model = virusModel
        self.workplaces = list()
        self.homes = list()
        self.schools = list()
        self.others = list()
    
    def placeAgents(self):
        agents = self.model.getAgents()

        newHome = Home()
        newSchool = School()
        newOther = Other()
        newWork = Work()

        self.homes.append(newHome)
        self.schools.append(newSchool)
        self.workplaces.append(newWork)
        self.others.append(newOther)

        for agent in agents:
            newHome.addMember(agent)
            newSchool.addMember(agent)
            newOther.addMember(agent)
            newWork.addMember(agent)
            
            agent.house = newHome
            agent.school = newSchool
            agent.other = newOther
            agent.work = newWork
            
            if newHome.full:
                newHome = Home()
                self.homes.append(newHome)
            if newSchool.full:
                newSchool = School()
                self.schools.append(newHome)
            if newOther.full:
                newOther = Other()
                self.others.append(newHome)
            if newWork.full:
                newWork = Work()
                self.workplaces.append(newHome)    




    
    
