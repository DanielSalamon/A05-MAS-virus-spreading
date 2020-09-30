import pandas as pd
import numpy as np


class DataCollector:

	def __init__(self):
		self.disease_data = {"susceptible" : [],
							 "exposed" : [],
							 "infected" : [],
							 "removed" : []} # we will be collecting data over time of simulation





	def print_overall_stats(self, model):

		agents_in_simulation = model.agents

		children = 0
		young = 0
		adult = 0
		old = 0

		susceptible = 0
		exposed = 0
		infected = 0
		removed = len(model.removed_agents)

		for agent in agents_in_simulation:

			status = agent.status
			age_group = agent.ageIndex

			if status == "susceptible":
				susceptible += 1
			elif status == "exposed":
				exposed += 1
			elif status == "infected":
				infected += 1


			if age_group == 0:
				children += 1
			elif age_group == 1:
				young += 1
			elif age_group == 2:
				adult += 1
			else:
				old += 1



		print("children: " + str(children))
		print("young: " + str(young))
		print("adults: " + str(adult))
		print("old " + str(old))
		print("susceptible: " + str(susceptible))
		print("exposed: " + str(exposed))
		print("infected: " + str(infected))
		print("removed: " + str(removed))
		print("**********************************")




	def collect_disease_stats_of_the_day(self, model):

		agents_in_simulation = model.agents
			

		susceptible = 0
		exposed = 0
		infected = 0
		removed = len(model.removed_agents)

		for agent in agents_in_simulation:

			status = agent.status
			age_group = agent.ageIndex

			if status == "susceptible":
				susceptible += 1
			elif status == "exposed":
				exposed += 1
			elif status == "infected":
				infected += 1


		#updating the disease data
		self.disease_data["susceptible"].append(susceptible)
		self.disease_data["exposed"].append(exposed)
		self.disease_data["infected"].append(infected)
		self.disease_data["removed"].append(removed)
		

	def simulation_summary(self):
		data_frame = pd.DataFrame.from_dict(self.disease_data)
		return data_frame