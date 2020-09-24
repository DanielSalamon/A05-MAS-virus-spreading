from mesa import Agent, Model
from mesa.time import RandomActivation
import numpy as np
from random import randint

class virusModel(Model):

  def __init__(self, popN):

      # We need to set the fixed values, based on research
      
      self.status = "susceptible"                    
      self.prob_infect = 0.5                
      self.prob_infected = 0.2              
      self.mask = False                   
      self.position = (1,0)  
      self.prob_death = 0.1 

  def step(self):
    self.schedule.step()
    print(self.status)

# t = transmission rate
# Cij = contatcts of agegroup j made by agegroup i
# k = 1-exp(-1\incubation period) -> daily probability of individual becoming infectious

    



