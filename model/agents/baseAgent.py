from mesa import Agent, Model
from random import randint

class BaseAgent(Agent): # Basic agent
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = ""                    # 4 possible states, based on paper: Susceptible, Exposed, Infected, Remove
        self.prob_infect = 0                # Probability of infect another agent
        self.prob_infected = 0              # Probability of getting infected
        self.chanceOfChange = 0
        self.transition = 0          
        self.mask = False                   # Wearing mask or not
        self.position = (randint(1,100), randint(1,100))               # Position on the map
        self.prob_death = 0.0               # Probability of dying by Covid-19


def change(self):
    if self.status == 'S':
        self.status == 'E'
    elif self.status == 'E':
        self.status == 'I'
    elif self.status == 'I':
        self.status == 'R'

def step(self):
    if self.status == 'S':
        pass            
    elif self.status == 'E':
        pass
    elif self.status == 'I':
        pass
    else:
        print("Im agent number: " + str(self.unique_id))
        print("My current position is: " + str(self.position) + "\n")