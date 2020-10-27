import model.virusModel as vm
import visualisation.dataCollector as dc
from visualisation.visualisation import *
from multiprocessing import Process
from tkinter import *
import os



DAYS = 100  # desired days the model will run


AGENTS = 1500  # desired agents the model will have

INIT_INFECTED = 15  # number of agents infected at the beggining of the simulation

# proportion of agents wearing a mask {'all', 'most', 'half', 'few', 'none'}
MASKCHANCE = 'all'

# choose how strict the lockdown is taken into account for each agegroup
SETTINGS = [False, 'severe', 'severe', 'severe', 'severe']
# choose restrictions as follows: {'none','minimal','moderate','severe,'total'}
# index0 = whether school is out or not
# index1 = restrictions for children
# index2 = restrictions for youngadults
# index 3 = restrictions for adults
# index 4 = restrictions for elderly


def MainProgram(simSettings, live_graph=True, vis=True, table=False, config=None):
    agents = simSettings[0]
    maskChance = simSettings[1]
    infected = simSettings[2]
    settings = simSettings[3]
    print(simSettings)

    model = vm.VirusModel(agents, maskChance, infected, settings)
    data_collector = dc.DataCollector()

    for day in range(1, DAYS + 1):
        print('Day ' + str(day))
        model.step()
        data_collector.print_overall_stats(model)
        if live_graph:
            data_collector.write_to_file(model)
        data_collector.collect_daily_data(model)

    if vis:
        # Summary of the simulation
        data_collector.print_summary()
        dead_agents = data_collector.total_dead_agents(model)
        recovered_agents = data_collector.total_recovered_agents(model)

        # Visualisation
        summary = data_collector.simulation_summary()
        perform_visualisation(summary, dead_agents, recovered_agents)
    if table:
        settings = (f'{config[0]}, {config[1]}, {config[2]}, {config[3]}, {config[4]}, {config[5]}')
        data_collector.totalSummary(model, settings)


def constructSettings(settings):
    newSettings = list()
    for agentType in range(1, 5):
        amount = getValue(settings[agentType])
        subsetting = [settings[0], amount, amount, amount]
        newSettings.append(subsetting)
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


def getMaskChance(maskChance):
    chance = maskChance.lower()
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


def runSingle():

    settings = constructSettings(SETTINGS)
    maskChance = getMaskChance(MASKCHANCE)
    agents = AGENTS
    infected = INIT_INFECTED
    simSettings = [agents, maskChance, infected, settings]
    live_graph_status = True

    if live_graph_status:
        f = open("visualisation/visual_data.txt", "w")
        f.close()

        p = Process(target=live_animation, args=[DAYS])
        p.start()
        MainProgram(simSettings, live_graph=live_graph_status)
        p.join()

        os.remove("visualisation/visual_data.txt")

    else:
        MainProgram(simSettings, live_graph=False)


def runComplete():
    #os.remove("data/totalSummary.txt")
	#mask = ['all', 'most', 'half', 'few', 'none']
	#lockdown = ['none', 'minimal', 'moderate', 'severe', 'total']
	#agent = [1, 2, 3, 4]

    #school = [True, False]
    #simSets = [False, 'none', 'none', 'none', 'none']
    school = [False]
    mask = ['few']
    lockdown = ['none', 'minimal', 'moderate', 'severe']
    simSets = ['none', 'none',] #younger older


    for i in range(5):
	    for s in school:
	        for m in mask:
	            for young in lockdown:
	                for old in lockdown:
	                    config = [m,s,young,young,young,old]
	                    settings = constructSettings([s,young, young, young, old])
	                    maskChance = getMaskChance(m)
	                    agents = AGENTS
	                    infected = INIT_INFECTED
	                    simSettings = [agents, maskChance, infected, settings]
	                    MainProgram(simSettings, live_graph=False, vis=False, table=True,config=config)



if __name__ == '__main__':

    runSingle()
    #runComplete()
