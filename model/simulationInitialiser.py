from model.areas import Home, Other, School, Work, All
from model.agents.baseAgent import *


class SimulationInitialiser(): 

    def __init__(self, virusModel):

        self.model = virusModel
        self.workplaces = list() # list of each area in the simulation 
        self.homes = list()
        self.schools = list()
        self.others = list()
        self.all = list()

    def placeAgents(self): # creates new instances of areas if full, adds each agent of the sim to each location with free spot
        agents = self.model.agents
        idNum = 1

        newHome = Home()
        newSchool = School()
        newOther = Other()
        newWork = Work()
        newAll = All()

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
