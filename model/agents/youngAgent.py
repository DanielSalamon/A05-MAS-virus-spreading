from model.agents.baseAgent import BaseAgent

class YoungAgent(BaseAgent):

  def __init__(self, unique_id, model, contactMatrix):
      super().__init__(unique_id, model, contactMatrix)

      # We need to set the fixed values, based on research
      
      self.status = "susceptible"                    
      self.prob_infect = 0.5                
      self.prob_infected = 0.2              
      self.mask = False                   
      self.position = (1,0)  
      self.prob_death = 0.1 

  def step(self):
    print(self.status)