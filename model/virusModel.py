import numpy as np
import random as rand
from mesa.datacollection import DataCollector
from mesa import Model, Agent
from mesa.time import RandomActivation
from model.fileIO.readData import getContactMatrices
from model.fileIO.readData import getPop
from model.simulationInitialiser import SimulationInitialiser
from model.agents import BaseAgent, ChildAgent, AdultAgent, YoungAgent, OldAgent

CONTACTMATRIX = getContactMatrices()
POP  = getPop()
# social distancing behaviours for different agents in different settings
CHILDSETTINGS = [False, 1, 1, 1] #schoolOut, allScale, workScale, otherScale
YOUNGSETTINGS = [False, 1, 1, 1]
ADULTSETTINGS = [False, 1, 1, 1]
ELDERLYSETTINGS = [False, 1, 1, 1]


class VirusModel(Model): # actual simulation 

    def __init__(self, popSize, maskChance, init_infected, settings ):
        self.popN, self.newPop = getPopDistribution(popSize) #total number of agents, list of number of agents per type
        self.maskChance = maskChance
        self.initially_infected = init_infected # number of infected agents at the beggining of simulation
        self.schedule = RandomActivation(self) # mesa schedule, agents activate in random order 
        self.agents = createPopulation(self, self.newPop, self.initially_infected) # population of agents created and stored
        self.simInit = SimulationInitialiser(self) # initialise agent locations and memberships to locations
        self.simInit.placeAgents()
        self.removed_agents = list() # list of dead agents
        self.totalInfected = 0
        self.totalExposed = 0
        self.totalRecovered = 0
        self.settings = settings
        for agent in self.agents: # initialise the agent meeting plans and add them to step schedule
            self.schedule.add(agent)
            agent.findMeetingNum()
            manipulateAgent(self, agent) # change social distancing behaviours if necessary

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
                    self.totalInfected += 1
                    agent.incubation_counter = 0
            else: 
                agent.incubation_counter += 1
        elif agent.status == "infected":
            if agent.incubation_counter == 7:
                if(agent.prob_death > rand.random()):
                    # probability of death or recover
                    agent.status = "removed"
                    self.agents.remove(agent)
                    agent.die()
                    self.removed_agents.append(agent.ageIndex) # append the age group of dead agent
                else:
                    agent.status = "recovered" #immune
                    self.totalRecovered += 1
                    agent.incubation_counter = 0 # average infection duration = 3-7 days
            
            else:
                agent.incubation_counter += 1


def gatherMeetings(virusModel): # collect number of meetings for later analysis
    agentMeetings = [
        agent.numberOfPeopleMet for agent in virusModel.schedule.agents]
    x = sum(agentMeetings)
    return x


def createPopulation(self, pop, initially_infected): # create a population according to real population distribution of the Netherlands
    iD = 0
    agents = list()
    for i in range(pop[0]):  # children
        newAgent = ChildAgent(iD, self, CONTACTMATRIX, self.maskChance)
        agents.append(newAgent)
        iD += 1
    for i in range(pop[1]):  # youngadults
        newAgent = YoungAgent(iD, self, CONTACTMATRIX, self.maskChance)
        agents.append(newAgent)
        iD += 1
    for i in range(pop[2]):  # adults
        newAgent = AdultAgent(iD, self, CONTACTMATRIX, self.maskChance)
        agents.append(newAgent)
        iD += 1
    for i in range(pop[3]):  # elderly
        newAgent = OldAgent(iD, self, CONTACTMATRIX, self.maskChance)
        agents.append(newAgent)
        iD += 1

    rand.shuffle(agents)

    # Take random sample ofa agents that will be infected at the beginning of the simulation
    for index in np.random.randint(len(agents), size=initially_infected):
        agents[index].status = "infected"

    return agents

    def manipulatepop(self):
        for agent in self.agents:
            manipulateAgent(self, agent)

def getPopDistribution(num = 1000):#get population distribution based off real data
    oldPopSize = sum(POP)
    newPopSize = num
    newPop = [0,0,0,0]
    for i in range(4):
        newPop[i] = int((POP[i]/oldPopSize) * newPopSize)
    
    return newPopSize, newPop

def manipulateAgent(self, agent): # set manipulation settings for certain agent
    if isinstance(agent, ChildAgent):
        agent.manipulationValues = self.settings[0]
    elif isinstance(agent, YoungAgent):
        agent.manipulationValues = self.settings[1]
    elif isinstance(agent, AdultAgent):
        agent.manipulationValues = self.settings[2]
    else:
        agent.manipulationValues = self.settings[3]

    agent.manipulate()


        

