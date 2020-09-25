from mesa import Agent, Model
from random import randint
import random as rand
import pandas as pd
import numpy as np

class BaseAgent(Agent): # Basic agent
    
    def __init__(self, unique_id, model, contactMatrix):
        super().__init__(unique_id, model)
        self.status = ""                    # 4 possible states, based on paper: Susceptible, Exposed, Infected, Remove
        self.prob_infect = 0                # Probability of infect another agent
        self.prob_infected = 0              # Probability of getting infected
        self.chanceOfChange = 0
        self.transition = 0          
        self.mask = False                   # Wearing mask or not
        self.position = (randint(1,100), randint(1,100))               # Position on the map
        self.prob_death = 0.0               # Probability of dying by Covid-19

        self.contactMatrix = contactMatrix
        self.toMeet = pd.DataFrame(np.zeros((5, 4)),index=['all', 'home', 'work','school','other'])
        #self.haveMet = pd.DataFrame(np.zeros((5, 4)),index=['all', 'home', 'work','school','other'])
        self.toMeet.columns = ['child', 'youngAdult', 'adult','old']
        #self.haveMet.columns = ['child', 'youngAdult', 'adult','old']
        self.toMeetTotal = 0

        self.ageIndex = 1
    
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
            findMeetingNum(self)
            print(self.toMeet)
            print(self.toMeetTotal)
            print("Im agent number: " + str(self.unique_id))
            print("My current position is: " + str(self.position) + "\n")

    def infected(self):
        self.status = "I"
    

def meetingChance(self, num):
    remainder = num%1
    people = num - remainder 
    if(remainder > rand.random()):
        people += 1
    people = int(people)
    return people

def findMeetingNum(self):
    ageindex = 0
    settingindex = 0
    for settings in self.contactMatrix:
        for people in settings.iloc[self.ageIndex,:]:
            self.toMeet.iloc[settingindex,ageindex] = meetingChance(self,people)
            ageindex += 1
        ageindex = 0
        settingindex += 1
    self.toMeetTotal = self.toMeet.values.sum()

def getToMeet(self):
    return self.toMeet

