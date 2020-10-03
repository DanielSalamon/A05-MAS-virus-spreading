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
        self.prob_infected = 0              # Probability of getting infected
        self.chanceOfChange = 0
        self.transition_to_infected = 1 - np.exp(-1/6) # from paper, average incubation period: 4-6 days
        self.transition_to_removed = 1 - (1-np.exp(-1/7)) # according to paper, probability of recover = 1 - exp(1/di)
                                                         # where di is average infection duration
        self.incubation_counter = 0
        self.mask = False                   # Wearing mask or not
        self.position = (randint(1, 100), randint(1, 100)
                         )               # Position on the map
        self.prob_death = 0.0
        # Probability of dying by Covid-19

        self.contactMatrix = contactMatrix
        self.toMeet = pd.DataFrame(np.zeros((5, 4)), index=[
                                   'all', 'house', 'work', 'school', 'other'])
        self.toMeet.columns = ['child', 'youngAdult', 'adult', 'old']
        self.settings = ['all', 'house', 'work', 'school', 'other']
        self.ageIndex = 0
        self.numberOfPeopleMet = 0
        self.peopleMet = [0, 0]
        self.countdown = 0

        self.day = 0

    def change(self):
        if self.status == 'S':
            self.status == 'E'
        elif self.status == 'E':
            self.status == 'I'
        elif self.status == 'I':
            self.status == 'R'

    def step(self):
        if self.status == 'S':
            print('a')
        elif self.status == 'E':
            print('a')
        elif self.status == 'I':
            print('a')
        else:
            self.day += 1
            self.peopleMet *= 0
            self.numberOfPeopleMet = 0
            # print(self.toMeet)
            pickAgents(self)
            #print("Im agent number: " + str(self.unique_id))
            #print("   I met " + str(self.numberOfPeopleMet) + " today!")

    def infected(self):
        self.status = "I"


def meetingChance(self, num):
    remainder = num % 1
    people = num - remainder
    if(remainder > rand.random()):
        people += 1
    people = int(people)
    return people


def findMeetingNum(self):
    ageindex = 0
    settingindex = 0
    for settings in self.contactMatrix:
        for people in settings[self.ageIndex, :]:
            self.toMeet.iloc[settingindex,
                             ageindex] = meetingChance(self, people)
            ageindex += 1
        ageindex = 0
        settingindex += 1
    self.toMeetTotal = self.toMeet.values.sum()


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

