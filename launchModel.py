import model.virusModel as vm
import visualisation.dataCollector as dc
from visualisation.visualisation import *
from multiprocessing import Process
from tkinter import *
import os


DAYS = 50 # desired days the model will run

AGENTS = 1000 # desired agents the model will have

INIT_INFECTED = 10 # number of agents infected at the beggining of the simulation

MASKCHANCE = 'all' # proportion of agents wearing a mask {'all', 'most', 'half', 'few', 'none'}

SETTINGS = [False, 'none', 'none', 'none', 'none'] # choose how strict the lockdown is taken into account for each agegroup 
							   # choose restrictions as follows: {'none','minimal','moderate','severe,'total'}
							   # index0 = whether school is out or not
							   # index1 = restrictions for children
							   # index2 = restrictions for youngadults
							   # index 3 = restrictions for adults
							   # index 4 = restrictions for elderly


def MainProgram(live_graph = True):
	settings = constructSettings()
	maskChance = getMaskChance()

	model = vm.VirusModel(AGENTS, maskChance, INIT_INFECTED, settings)
	data_collector = dc.DataCollector()

	for day in range(1, DAYS + 2):
	    print('Day '+ str(day))
	    model.step()
	    data_collector.print_overall_stats(model)
	    if live_graph:
	    	data_collector.write_to_file(model)
	    data_collector.collect_daily_data(model)


	# Summary of the simulation

	data_collector.print_summary()
	df = data_collector.total_dead_agents(model)

	# Visualisation

	summary = data_collector.simulation_summary()
	perform_visualisation(summary, df)

def constructSettings():
	settings = SETTINGS
	newSettings = list()
	for agentType in range(1,5):
		amount = getValue(settings[agentType])
		subsetting = [settings[0], amount, amount, amount]
		newSettings.append(subsetting)
	print(newSettings)
	return newSettings

def getValue(severity):
	sev = severity.lower()
	noMeasure = 1
	minimal = 0.8
	moderate = 0.5
	severe = 0.2
	total = 0
	if sev == 'minimal':
		return minimal
	elif sev == 'moderate':
		return moderate
	elif sev == 'severe':
		return severe
	elif sev == 'total':
		return total
	else:
		return noMeasure

def getMaskChance():
	chance = MASKCHANCE.lower()
	none = 0
	few = 0.2
	half = 0.5
	most = 0.8
	all = 1
	if chance == 'few':
		return few
	elif chance == 'half':
		return half
	elif chance == 'most':
		return most
	elif chance == 'all':
		return all
	else:
		return none


def begin():
	live_graph_status = True

	if live_graph_status :
	    f = open("visualisation/visual_data.txt", "w")
	    f.close()

	    p = Process(target=live_animation,args = [DAYS])
	    p.start()
	    MainProgram(live_graph=live_graph_status)
	    p.join()

	    os.remove("visualisation/visual_data.txt")

	else:			
		MainProgram(live_graph=False)

if __name__ == '__main__':
	
	begin()

