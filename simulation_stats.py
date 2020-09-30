

def print_stats(model):

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




