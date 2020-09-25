from model.agents import baseAgent
import areas as ar
import virusModel as vm

class Places():

    def __init__(self, model):

        self.model = model
        self.workplaces = list()
        self.homes = list()
        self.schools = list()
        self.others = list()
    
    def placeAgents():
        agents = vm.getAgents()

        newHome = ar.Home()
        newSchool = ar.School()
        newOther = ar.Other()
        newWork = ar.Work()

        self.homes.append(newHome)
        self.schools.append(newSchool)
        self.workplaces.append(newWork)
        self.others.append(newOther)

        for agent in agents:
            newHome.addMember(agent)
            newSchool.addMember(agent)
            newOther.addMember(agent)
            newWork.addMember(agent)

            
            if newHome.isFull():
                newHome = ar.Home()
                self.append(newHome)
            if newSchool.isFull():
                newSchool = ar.School()
                self.append(newHome)
            if newOther.isFull():
                newOther = ar.Other()
                self.append(newHome)
            if newWork.isFull():
                newWork = ar.Work()
                self.append(newHome)    




    
    
