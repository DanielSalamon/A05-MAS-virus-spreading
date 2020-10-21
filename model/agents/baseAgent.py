from mesa import Agent, Model
from random import randint
import random as rand
import pandas as pd
import numpy as np


class BaseAgent(Agent):  # Basic agent
    def __init__(self, unique_id, model, contactMatrix,maskChance):
        super().__init__(unique_id, model)
        # 4 possible states, based on paper: Susceptible, Exposed, Infected, Remove
        self.status = ""
        self.contactMatrix = contactMatrix
        self.chanceOfChange = 0
        self.transition_to_infected = 1 - np.exp(-1/6) # from paper, average incubation period: 4-6 days
        
        self.incubation_counter = 0
        self.prob_death = 0.0 # Probability of dying by Covid-19
        
        self.toMeet = pd.DataFrame(np.zeros((5, 4)), index=['all', 'house', 'work', 'school', 'other']) #meeting lists for each agent
        self.toMeetBase = pd.DataFrame(np.zeros((5, 4)), index=['all', 'house', 'work', 'school', 'other'])
        self.toMeet.columns = ['child', 'youngAdult', 'adult', 'old']
        self.toMeetBase.columns = ['child', 'youngAdult', 'adult', 'old']

        self.settings = ['all', 'house', 'work', 'school', 'other'] # list of all places agent belongs (later initialised to objects)

        self.ageIndex = 0

        self.numberOfPeopleMet = 0
        self.peopleMet = [0, 0]
        self.countdown = 0

        self.manipulationValues = [False, 1, 1, 1] # referrs to the social distancing strategies an agent adopts

        if maskChance > rand.random():
            self.mask = True # Wearing mask or not NOT YET IMPLEMENTED IN CODE 
        else:
            self.mask + False

            
    def step(self):
        self.peopleMet *= 0 # reset list of met agents to empty
        self.numberOfPeopleMet = 0 #reset number of people met to 0
        #print(self.toMeetBase)
        pickAgents(self) # find agents to meet
    
    def manipulate(self): # function to change the meetings list for specific locations
        schoolOut = self.manipulationValues[0] # boolean to indicate whether school has been suspended

        allScale = self.manipulationValues[1]   # next three are a scaler by which the contacts will be multiplied 0 - 1 
        workScale = self.manipulationValues[2]  # 1 indicates nothing changes and 0 indicated that no contacts will be made
        otherScale = self.manipulationValues[3]
        schoolScale = 1
        houseScale = 1

        temp = self.toMeetBase

        if schoolOut: #set school meetings to off or on
            schoolScale = 0
        temp = temp.mul([allScale,houseScale,workScale,schoolScale,otherScale], axis = 0)
        self.toMeet = temp
    
    def findMeetingNum(self): # create the meeting list according to contact matrix, happens when agents are initialised to the model
        ageindex = 0
        settingindex = 0
        for settings in self.contactMatrix:
            for people in settings[self.ageIndex, :]:
                self.toMeetBase.iloc[settingindex, ageindex] = people
                ageindex += 1
            ageindex = 0
            settingindex += 1
        self.toMeetTotal = self.toMeetBase.values.sum()
    
    def die(self):  # if agent dies it must be removed from all of its locations
        for location in self.settings:
            location.removeAgent(self)


def meetingChance(self, num): # helper function to deal with decimals
    remainder = num % 1 # chance of meeting an extra agent based on decimal
    people = num - remainder # natural number correspinding to people an agent will meet
    if(remainder > rand.random()):
        people += 1
    people = int(people)
    return people


def pickAgents(self): # selects a random agents according to agents meeting list
    settingIndex = 0
    peopleIndex = 0
    for settingIndex in range(4):
        for peopleIndex in range(4):
            people = round(self.toMeet.iloc[settingIndex, peopleIndex])
            self.countdown = meetingChance(self, people)
            if self.countdown > 0:
                while not self.countdown <= 0:
                    meetAtLocation(self, settingIndex, peopleIndex)


def meetAtLocation(self, locationIndex, personIndex): #collects the agent to meet and the location to meet at
    person = False
    location = self.settings[locationIndex]
    person = getPerson(self, personIndex, location)
    if person:
        if not person == self and not person.unique_id in self.peopleMet: # if the agent picked exists and is not self, meet that person
            contact(self, person, location)
    self.countdown -= 1


def getPerson(self, personIndex, location): # select person of certain type from location member lists
    agentType = location.members[personIndex]
    if len(agentType) > 0:
        return getRandomMem(agentType, len(agentType))


def getRandomMem(ageGroup, memNum): # helper function to get random member out of list
    randomMemLocation = rand.randint(0, memNum-1)
    return ageGroup[randomMemLocation]


def contact(self, agent, location): # make contact with an agent 
    self.peopleMet.append(agent.unique_id)
    location.meet(self, agent)
    self.numberOfPeopleMet += 1


