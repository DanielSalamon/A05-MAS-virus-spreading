from mesa import Agent, Model
from random import randint
import random as rand
import pandas as pd
import numpy as np


class BaseAgent(Agent):  # Basic agent
    def __init__(self, unique_id, model, contactMatrix):
        super().__init__(unique_id, model)
        # 4 possible states, based on paper: Susceptible, Exposed, Infected, Remove
        self.status = ""
        self.prob_infect = 0                # Probability of infect another agent
        self.prob_infected = 0.2              # Probability of getting infected
        self.chanceOfChange = 0
        self.transition = 0
        self.transition_to_removed = 0
        self.mask = False                   # Wearing mask or not
        self.position = (randint(1, 100), randint(1, 100)
                         )               # Position on the map
        self.prob_death = 0.0
        # Probability of dying by Covid-19

        self.contactMatrix = contactMatrix
        self.toMeet = pd.DataFrame(np.zeros((5, 4)), index=['all', 'house', 'work', 'school', 'other'])
        self.toMeetBase = pd.DataFrame(np.zeros((5, 4)), index=['all', 'house', 'work', 'school', 'other'])
        self.toMeet.columns = ['child', 'youngAdult', 'adult', 'old']
        self.toMeetBase.columns = ['child', 'youngAdult', 'adult', 'old']

        self.settings = ['all', 'house', 'work', 'school', 'other']
        self.ageIndex = 0
        self.numberOfPeopleMet = 0
        self.peopleMet = [0, 0]
        self.countdown = 0
        self.day = 0

        self.manipulationValues = [False, 1, 1, 1]

    def change(self):
        if self.status == 'S':
            self.status == 'E'
        elif self.status == 'E':
            self.status == 'I'
        elif self.status == 'I':
            self.status == 'R'

    def step(self):
        self.day += 1
        self.peopleMet *= 0
        self.numberOfPeopleMet = 0
        #print(self.toMeetBase)
        pickAgents(self)

    def infected(self):
        self.status = "I"
    
    def manipulate(self):
        temp = self.toMeetBase

        if self.manipulationValues[0]: #set school meetings to off or on
            temp.iloc[3,:] *= 0
        temp.iloc[0,:] *= round(temp.iloc[0,:]* self.manipulationValues[1]) # scale meetings in general by certain value
        temp.iloc[2,:] *= round(temp.iloc[0,:]* self.manipulationValues[2]) # scale meetings at work by certain value
        temp.iloc[4,:] *= round(temp.iloc[0,:]* self.manipulationValues[3]) # scale meetings at other by certain value

        self.toMeet = temp
    
    def findMeetingNum(self):
        ageindex = 0
        settingindex = 0
        for settings in self.contactMatrix:
            for people in settings[self.ageIndex, :]:
                self.toMeetBase.iloc[settingindex,
                                ageindex] = meetingChance(self, people)
                ageindex += 1
            ageindex = 0
            settingindex += 1
        self.toMeetTotal = self.toMeetBase.values.sum()
        self.manipulate()


def meetingChance(self, num):
    remainder = num % 1
    people = num - remainder
    if(remainder > rand.random()):
        people += 1
    people = int(people)
    return people





def pickAgents(self):
    settingIndex = 0
    peopleIndex = 0
    for settingIndex in range(4):
        for peopleIndex in range(4):
            self.countdown = self.toMeet.iloc[settingIndex, peopleIndex]
            if self.countdown > 0:
                while not self.countdown <= 0:
                    meetAtLocation(self, settingIndex, peopleIndex)


def meetAtLocation(self, locationIndex, personIndex):
    person = False
    location = self.settings[locationIndex]
    person = getPerson(self, personIndex, location)
    if person:
        if not person == self and not person.unique_id in self.peopleMet:
            contact(self, person, location)
    self.countdown -= 1


def getPerson(self, personIndex, location):
    agentType = location.members[personIndex]
    if len(agentType) > 0:
        return getRandomMem(agentType, len(agentType))


def getRandomMem(ageGroup, memNum):
    randomMemLocation = rand.randint(0, memNum-1)
    return ageGroup[randomMemLocation]


def contact(self, agent, location):
    # print(location.areaType)
    self.peopleMet.append(agent.unique_id)
    location.meet(self, agent)
    self.numberOfPeopleMet += 1


