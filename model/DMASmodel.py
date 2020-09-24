from mesa import Agent, Model
from mesa.time import RandomActivation
import numpy as np
from random import randint
from agents import BaseAgent


class VirusModel(Model):

    def __init__(self, popN):

        self.popN = popN
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.popN):
            a = BaseAgent(i, self)
            self.schedule.add(a)


def step(self):
    self.schedule.step()
    print(self.status)

# t = transmission rate
# Cij = contatcts of agegroup j made by agegroup i
# k = 1-exp(-1\incubation period) -> daily probability of individual becoming infectious
