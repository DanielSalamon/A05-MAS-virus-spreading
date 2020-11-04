import pandas as pd


class DataCollector:

	def __init__(self):
		self.highestExposed = 0
		self.highestInfected = 0
		self.highestDead = 0
		self.numberOfDeadYesterday = 0

		self.population_data = {"susceptible" : [],
							 "exposed" : [],
							 "infected" : [],
							 "removed" : [],
							 "recovered" : []} # we will be collecting data over time of simulation


		# for colleting data of each age group
		self.children_data = {"susceptible" : [],
							 "exposed" : [],
							 "infected" : [],
							 "removed" : [],
							 "recovered" : []}

		self.young_data = {"susceptible" : [],
							 "exposed" : [],
							 "infected" : [],
							 "removed" : [],
							 "recovered" : []}

		self.adult_data = {"susceptible" : [],
							 "exposed" : [],
							 "infected" : [],
							 "removed" : [],
							 "recovered" : []}

		self.old_data = {"susceptible" : [],
							 "exposed" : [],
							 "infected" : [],
							 "removed" : [],
							 "recovered" : []}


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
		recovered = 0

		for agent in agents_in_simulation:

			status = agent.status
			age_group = agent.ageIndex

			if status == "susceptible":
				susceptible += 1
			elif status == "exposed":
				exposed += 1
			elif status == "infected":
				infected += 1
			elif status == "recovered":
				recovered += 1


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
		print("recovered: " + str(recovered))
		print("**********************************")


	def write_to_file(self,model):
		agents_in_simulation = model.agents

		children = 0
		young = 0
		adult = 0
		old = 0

		susceptible = 0
		exposed = 0
		infected = 0
		removed = len(model.removed_agents)
		recovered = 0

		for agent in agents_in_simulation:

			status = agent.status
			age_group = agent.ageIndex

			if status == "susceptible":
				susceptible += 1
			elif status == "exposed":
				exposed += 1
			elif status == "infected":
				infected += 1
			elif status == "recovered":
				recovered += 1


			if age_group == 0:
				children += 1
			elif age_group == 1:
				young += 1
			elif age_group == 2:
				adult += 1
			else:
				old += 1

		f= open("visualisation/visual_data.txt", "a")
		f.write(str(children)+","+str(young)+","+str(adult)+","+str(old)+","+str(susceptible)+","+str(exposed)+","+str(infected)+","+str(removed)+","+str(recovered)+"\n")

		f.close()




	def collect_disease_stats_of_the_day(self, model):

		agents_in_simulation = model.agents
			

		susceptible = 0
		exposed = 0
		infected = 0
		removed = len(model.removed_agents)
		recovered = 0

		for agent in agents_in_simulation:

			status = agent.status
			age_group = agent.ageIndex

			if status == "susceptible":
				susceptible += 1
			elif status == "exposed":
				exposed += 1
			elif status == "infected":
				infected += 1
			elif status == "recovered":
				recovered += 1

		

		if exposed > self.highestExposed:
			self.highestExposed = exposed
		if infected > self.highestInfected:
			self.highestInfected = infected
		if (removed - self.numberOfDeadYesterday) > self.highestDead:
			self.highestDead = (removed - self.numberOfDeadYesterday)

		self.numberOfDeadYesterday = removed

		#updating the disease data
		self.population_data["susceptible"].append(susceptible)
		self.population_data["exposed"].append(exposed)
		self.population_data["infected"].append(infected)
		self.population_data["removed"].append(removed)
		self.population_data["recovered"].append(recovered)
		

	def update_dict(self, age_groups_stats, dict_to_update, age_group): # helper function


		dict_to_update["susceptible"].append(age_groups_stats[age_group][0])
		dict_to_update["exposed"].append(age_groups_stats[age_group][1])
		dict_to_update["infected"].append(age_groups_stats[age_group][2])
		dict_to_update["removed"].append(age_groups_stats[age_group][3])
		dict_to_update["recovered"].append(age_groups_stats[age_group][4])

	def collect_disease_stats_by_age_group(self, model):

		age_groups_stats = {0 : [0,0,0,0,0], # children : suceptible, exposed, infected, removed, recovered
							1 : [0,0,0,0,0], # young 
							2 : [0,0,0,0,0], # adults
							3 : [0,0,0,0,0]} # old

		for agent in model.agents:

			status = agent.status
			agent_age = agent.ageIndex

			if status == "susceptible":
				age_groups_stats[agent_age][0] += 1
			elif status == "exposed":
				age_groups_stats[agent_age][1] += 1
			elif status == "infected":
				age_groups_stats[agent_age][2] += 1
			elif status == "recovered":
				age_groups_stats[agent_age][4] += 1


		for age in model.removed_agents: # we keep only ages of dead agents in model.removed_agents
			age_groups_stats[age][3] += 1
			


		list_of_dicts = [self.children_data, self.young_data, self.adult_data, self.old_data]
		for dic in range(len(list_of_dicts)):
			self.update_dict(age_groups_stats, list_of_dicts[dic], dic)



	def collect_daily_data(self, model):
		self.collect_disease_stats_by_age_group(model)
		self.collect_disease_stats_of_the_day(model)


	def simulation_summary(self):
		population_frame = pd.DataFrame.from_dict(self.population_data)
		children_frame = pd.DataFrame.from_dict(self.children_data)
		young_frame = pd.DataFrame.from_dict(self.young_data)
		adult_frame = pd.DataFrame.from_dict(self.adult_data)
		old_frame = pd.DataFrame.from_dict(self.old_data)

		return population_frame, children_frame, young_frame, adult_frame, old_frame


	def print_summary(self):

		summary = self.simulation_summary()
		print("------------------SUMMARIES--------------------\n")
		print("Population summary: \n")
		print(summary[0].tail(1))
		print("-----------------------------------------------")
		print("Children summary: \n")
		print(summary[1].tail(1))
		print("-----------------------------------------------")
		print("Young summary: \n")
		print(summary[2].tail(1))
		print("-----------------------------------------------")
		print("Adults summary: \n")
		print(summary[3].tail(1))
		print("-----------------------------------------------")
		print("Olds summary: \n")
		print(summary[4].tail(1))
		print("-----------------------------------------------")
		
		
		

	def total_dead_agents(self, model):

		dead_agents = {0 : [0],
					   1 : [0],
					   2 : [0],
					   3 : [0]}

		for age in model.removed_agents:
			dead_agents[age][0] += 1


		data_frame = pd.DataFrame.from_dict(dead_agents)
		data_frame.columns = ["Children", "Young", "Adults", "Olds"]

		print("Total dead agents: \n")
		print(data_frame)

		return dead_agents

	def total_recovered_agents(self, model):

		recovered_agents = {0 : [0],
					   		1 : [0],
					  		2 : [0],
					   		3 : [0]}

		for agent in model.agents:

			status = agent.status
			age_group = agent.ageIndex

			if status == "recovered":
				recovered_agents[age_group][0] += 1
				

		data_frame = pd.DataFrame.from_dict(recovered_agents)
		data_frame.columns = ["Children", "Young", "Adults", "Olds"]

		print("Total recovered agents: \n")
		print(data_frame)

		return recovered_agents

	def totalSummary(self, model, settings):
		
		# total number of people died
		totalDead = len(model.removed_agents)
		# total number of people infected
		totalInfected = model.totalInfected
		# total number of people exposed
		totalExposed = model.totalExposed
		# highest number of infected in a day
		highestDead = self.highestDead
		# highest number of dead in a day
		highestExposed = self.highestExposed
		# highest number of exposed in a day
		highestInfected = self.highestInfected
		# total recovered
		totalRecovered = model.totalRecovered

		with open('data/totalSummary.txt', 'a') as file:
			file.write(str(settings)+","+str(totalExposed)+","+str(totalInfected)+","+str(totalDead)+","+str(totalRecovered)+","+str(highestExposed)+","+str(highestInfected)+","+str(highestDead)+"\n")
