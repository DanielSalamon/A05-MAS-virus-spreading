from model.agents.baseAgent import BaseAgent

class ChildAgent(BaseAgent):

  def __init__(self, unique_id, model, contactMatrix):
      super().__init__(unique_id, model, contactMatrix)
      self.ageIndex = 0
      # We need to set the fixed values, based on research
      self.status = "infected"                    
      self.prob_infect = 1               
      self.prob_infected = 0.3            
      self.mask = False                   
      self.position = (1,0)  
      self.prob_death = 0.1 
