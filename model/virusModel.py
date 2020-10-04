import numpy as np
import random as rand
from mesa.datacollection import DataCollector
from mesa import Model, Agent
from mesa.time import RandomActivation
from model.fileIO.readData import getContactMatrices
from model.fileIO.readData import getPop
from model.places import Places
from model.agents import BaseAgent, ChildAgent, AdultAgent, YoungAgent, OldAgent

CONTACTMATRIX = getContactMatrices()
POP  = getPop()
POPSIZE = 1000
CHILDSETTINGS = [True, 0.5, 0.5, 0.5] #schoolOut, allScale, workScale, otherScale
YOUNGSETTINGS = [True, 0.5, 0.5, 0.5]
ADULTSETTINGS = [True, 0.5, 0.5, 0.5]
ELDERLYSETTINGS = [True, 0.5, 0.5, 0.5]


class VirusModel(Model):

    def __init__(self):
        self.popN, self.newPop = getPopDistribution(POPSIZE)
        self.schedule = RandomActivation(self)
        self.agents = createPopulation(self, self.newPop)
        self.places = Places(self)
        self.places.placeAgents()
        self.removed_agents = list()
        for agent in self.agents:
            self.schedule.add(agent)
            agent.findMeetingNum()
            manipulateAgent(agent)

    def getAgents(self):
        return self.agents

    def step(self):

        # firstly, calculate transitions for all agents in simulation:
        for agent in self.agents:
            self.transition(agent)

        # Secondly, do all of the meetings of current day:
        self.schedule.step()
        print(gatherMeetings(self))
    
    def transition(self,agent):
        if agent.status == "exposed":
            if agent.incubation_counter == 6: # average incubation period = 4-6 days
                if(agent.transition_to_infected > rand.random()):   # probability of Exposed -> Infected
                    agent.status = "infected"
                    agent.incubation_counter = 0
            else: 
                agent.incubation_counter += 1
        elif agent.status == "infected":
            if agent.incubation_counter == 7: # average infection duration = 3-7 days
                if(agent.prob_death > rand.random()):  # probability of death or recover
                    agent.status = "removed"
                    self.agents.remove(agent)
                    agent.die()
                    self.removed_agents.append(agent.ageIndex) # append the age group of dead agent
                else: 
                    agent.status = "susceptible"
                    agent.incubation_counter = 0
            else:
                agent.incubation_counter += 1


def gatherMeetings(virusModel):
    agentMeetings = [
        agent.numberOfPeopleMet for agent in virusModel.schedule.agents]
    x = sum(agentMeetings)
    return x


def createPopulation(self, pop):
    iD = 0
    agents = list()
    for i in range(pop[0]):  # children
        newAgent = ChildAgent(iD, self, CONTACTMATRIX)
        agents.append(newAgent)
        iD += 1
    for i in range(pop[1]):  # youngadults
        newAgent = YoungAgent(iD, self, CONTACTMATRIX)
        agents.append(newAgent)
        iD += 1
    for i in range(pop[2]):  # adults
        newAgent = AdultAgent(iD, self, CONTACTMATRIX)
        agents.append(newAgent)
        iD += 1
    for i in range(pop[3]):  # elderly
        newAgent = OldAgent(iD, self, CONTACTMATRIX)
        agents.append(newAgent)
        iD += 1

    rand.shuffle(agents)

    # Take random sample ofa agents that will be infected at the beginning of the simulation
    for index in np.random.randint(len(agents), size=10):
        agents[index].status = "infected"

    return agents

    def manipulatepop(self):
        for agent in self.agents:
            manipulateAgent(agent)

def getPopDistribution(num = 1000):
    oldPopSize = sum(POP)
    newPopSize = num
    newPop = [0,0,0,0]
    for i in range(4):
        newPop[i] = int((POP[i]/oldPopSize) * newPopSize)
    print(newPop)
    return newPopSize, newPop

def manipulateAgent(agent):
    if isinstance(agent, ChildAgent):
        agent.manipulationValues = CHILDSETTINGS
    elif isinstance(agent, YoungAgent):
        agent.manipulationValues = YOUNGSETTINGS
    elif isinstance(agent, AdultAgent):
        agent.manipulationValues = ADULTSETTINGS
    else:
        agent.manipulationValues = ELDERLYSETTINGS

    agent.manipulate()


        

