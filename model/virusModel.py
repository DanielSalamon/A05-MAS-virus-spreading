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
CHILDSETTINGS = [False, .5,.5,.5] #schoolOut, allScale, workScale, otherScale
YOUNGSETTINGS = [False, .5,.5,.5]
ADULTSETTINGS = [False, 1,1,1]
ELDERLYSETTINGS = [False, .5,.5,.5]


class VirusModel(Model):

    def __init__(self):
        self.popN, self.newPop = getPopDistribution(200)
        self.schedule = RandomActivation(self)
        self.agents = createPopulation(self, self.newPop)
        self.places = Places(self)
        self.places.placeAgents()
        self.removed_agents = list()
        for agent in self.agents:
            self.schedule.add(agent)
            agent.findMeetingNum()

    def getAgents(self):
        return self.agents

    def step(self):

        # firstly, calculate transitions for all agents in simulation:
        for agent in self.agents:
            if agent.status == "exposed":
                if(agent.transition_to_infected > rand.random()):   # probability of Exposed -> Infected
                    agent.status = "infected"
            elif agent.status == "infected":
                if(agent.transition_to_removed * agent.prob_death > rand.random()):  # probability of death or recover
                    agent.status = "removed"
                    self.agents.remove(agent)
                    self.removed_agents.append(agent.ageIndex) # append the age group of dead agent
                else: 
                    agent.status = "susceptible"


        # Secondly, do all of the meetings of current day:
        self.schedule.step()
        print(gatherMeetings(self))


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

    index = np.random.randint(len(agents), size=100)
    for ind in index:
        agents[ind].status = "infected"

    return agents

def getPopDistribution(num = 1000):
    oldPopSize = sum(POP)
    newPopSize = num
    newPop = [0,0,0,0]
    for i in range(4):
        newPop[i] = int((POP[i]/oldPopSize) * newPopSize)
    print(newPop)
    return newPopSize, newPop

def manipulatePop(self):
    for agent in self.agents:
        if isinstance(agent, ChildAgent):
            agent.manipulationValues = CHILDSETTINGS
        elif isinstance(agent, YoungAgent):
            agent.manipulationValues = YOUNGSETTINGS
        elif isinstance(agent, AdultAgent):
            agent.manipulationValues = ADULTSETTINGS
        else:
            agent.manipulationValues = ELDERLYSETTINGS
        agent.manipulate()

        

