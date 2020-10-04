from model.agents.baseAgent import BaseAgent

class YoungAgent(BaseAgent):
  def __init__(self, unique_id, model, contactMatrix):
      super().__init__(unique_id, model, contactMatrix)
      self.ageIndex = 1
      # We need to set the fixed values, based on research
      self.status = "susceptible"                              
      self.mask = False                   
      self.position = (1,0)  
      self.prob_death = 7/33345 

      # prob_death based on the "Demographic of Covids Death" : https://dc-covid.site.ined.fr/en/data/netherlands/
      # and Distribution of Coronairus by age :https://www.statista.com/statistics/1176377/coronavirus-cases-by-age-group-in-the-netherlands/
      # Data indicates the situation of COVID on 29 September 2020 in Netherlands
