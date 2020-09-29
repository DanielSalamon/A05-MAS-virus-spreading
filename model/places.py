from model.areas import Home, Other, School, Work, All
from model.agents.baseAgent import *


class Places():

    def __init__(self, virusModel):

        self.model = virusModel
        self.workplaces = list()
        self.homes = list()
        self.schools = list()
        self.others = list()
        self.all = list()

    def placeAgents(self):
        agents = self.model.agents
        idNum = 1

        newHome = Home(1)
        newSchool = School(1)
        newOther = Other(1)
        newWork = Work(1)
        newAll = All(1)

        self.homes.append(newHome)
        self.schools.append(newSchool)
        self.workplaces.append(newWork)
        self.others.append(newOther)
        self.all.append(newAll)

        for agent in agents:
            newHome.addMember(agent)
            newSchool.addMember(agent)
            newOther.addMember(agent)
            newWork.addMember(agent)
            newAll.addMember(agent)

            agent.settings[0] = newAll
            agent.settings[1] = newHome
            agent.settings[2] = newWork
            agent.settings[3] = newSchool
            agent.settings[4] = newOther
            if newHome.full:
                newHome = Home(2)
                self.homes.append(newHome)
            if newSchool.full:
                newSchool = School(2)
                self.schools.append(newHome)
            if newOther.full:
                newOther = Other(2)
                self.others.append(newHome)
            if newWork.full:
                newWork = Work(2)
                self.workplaces.append(newHome)
