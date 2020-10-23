import model.virusModel as vm
import visualisation.dataCollector as dc
from visualisation.visualisation import *
from multiprocessing import Process
from tkinter import *
import os


DAYS = 50 # desired days model will run

AGENTS = 1000 # desired agents model will have

MASKCHANCE = 1.0 # proportion of agents wearing a mask

INIT_INFECTED = 10 # number of agents infected at the beggining of simulaiton

SETTINGS = [False, 'none', 'none', 'none', 'none'] # choose how strict lockdown is taken into account for each agegroup 
							   # choose restrictions as follows: 'none','minimal','moderate','severe,'total'
							   # index0 = whether school is out or not
							   # index1 = restrictions for children
							   # index2 = restrictions for youngadults
							   # index 3 = restrictions for adults
							   # index 4 = restrictions for elderly


def MainProgram(live_graph = True):

	model = vm.VirusModel(AGENTS, MASKCHANCE, INIT_INFECTED, constructSettings())
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
	if sev == 'none':
		return noMeasure
	elif sev == 'minimal':
		return minimal
	elif sev == 'moderate':
		return moderate
	elif sev == 'severe':
		return severe
	elif sev == 'total':
		return total
	else:
		return noMeasure


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

