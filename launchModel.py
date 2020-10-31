import model.virusModel as vm
import visualisation.dataCollector as dc
from visualisation.visualisation import *
from multiprocessing import Process
from tkinter import *
import os
import readchar



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

RUNTYPE = 'single'

LIVE_GRAPH_STATUS = True

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
    # live_graph_status = True

    if LIVE_GRAPH_STATUS:
        f = open("visualisation/visual_data.txt", "w")
        f.close()

        p = Process(target=live_animation, args=[DAYS])
        p.start()
        MainProgram(simSettings, live_graph=LIVE_GRAPH_STATUS)
        p.join()

        if os.path.isfile("visualisation/visual_data.txt"):
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


error_message = ""

def print_error_message():
    global error_message
    if error_message != "":
        print("NOTE: "+error_message)
        print("===================================\n")
        error_message = ""

def mapSettings(arguments):
    global DAYS
    global AGENTS
    global INIT_INFECTED
    global LIVE_GRAPH_STATUS
    global SETTINGS
    global MASKCHANCE
    global error_message


    # arguments = ''.join(arguments)
    arguments= arguments.replace(" ","")
    arguments = arguments.split(',')

    for argument in arguments:
        argument = argument.lower()
        argument = argument.split('=')

        if argument[0] == 'days':
            if argument[1].isnumeric():
                DAYS = int(argument[1])
            else:
                # print("Invalid number of Days entered, Using Default.")
                error_message+="Invalid number of Days entered, Using Default.\n"
        elif argument[0] == 'agents':
            if argument[1].isnumeric():
                AGENTS = int(argument[1])
            else:
                # print("Invalid number of Agents entered, Using Default.")
                error_message+="Invalid number of Agents entered, Using Default.\n"
        elif argument[0] == 'init_infected':
            if argument[1].isnumeric():
                INIT_INFECTED = int(argument[1])
            else:
                # print("Invalid number of Initial Infected entered, Using Default.")
                error_message+="Invalid number of Initial Infected entered, Using Default.\n"
        elif argument[0] == 'live_graph':
            if argument[1] =='true':
                LIVE_GRAPH_STATUS = True
            elif argument[1] == 'false':
                LIVE_GRAPH_STATUS = False
            else:
                # print("Invalid live graph status entered, Using Default.")
                error_message +="Invalid live graph status entered, Using Default.\n"
        elif argument[0] == 'school':
            if (argument[1] == 'true'):
                SETTINGS[0] = True
            elif (argument[1] == 'false'):
                SETTINGS[0] = False
            else:
                # print("Invalid school setting entered, Using Default.")
                error_message+="Invalid school setting entered, Using Default.\n"
        elif argument[0] == 'child':
            if (argument[1] == 'none') or (argument[1] == 'minimal') or (argument[1] == 'moderate') or (argument[1] == 'severe') or (argument[1] == 'total'):
                SETTINGS[1]=argument[1]
            else:
                # print("Invalid child lockdown setting entered, Using Default.")
                error_message+="Invalid child lockdown setting entered, Using Default.\n"
        elif argument[0] == 'young':
            if (argument[1] == 'none') or (argument[1] == 'minimal') or (argument[1] == 'moderate') or (argument[1] == 'severe') or (argument[1] == 'total'):
                SETTINGS[2]=argument[1]
            else:
                # print("Invalid young lockdown setting entered, Using Default.")
                error_message+="Invalid young lockdown setting entered, Using Default.\n"


        elif argument[0] == 'adult':
            if (argument[1] == 'none') or (argument[1] == 'minimal') or (argument[1] == 'moderate') or (argument[1] == 'severe') or (argument[1] == 'total'):
                SETTINGS[3]=argument[1]
            else:
                # print("Invalid adult lockdown setting entered, Using Default.")
                error_message+="Invalid adult lockdown setting entered, Using Default.\n"
        elif argument[0] == 'old':
            if (argument[1] == 'none') or (argument[1] == 'minimal') or (argument[1] == 'moderate') or (argument[1] == 'severe') or (argument[1] == 'total'):
                SETTINGS[4]=argument[1]
            else:
                # print("Invalid old lockdown setting entered, Using Default.")
                error_message+="Invalid old lockdown setting entered, Using Default.\n"
        elif argument[0] == 'mask_chance':
            if (argument[1] == 'all') or (argument[1] == 'most') or (argument[1] == 'half') or (argument[1] == 'few') or (argument[1] == 'none'):
                MASKCHANCE=argument[1]
            else:
                # print("Invalid MASK CHANCE setting entered, Using Default.")
                error_message+="Invalid MASK CHANCE setting entered, Using Default.\n"

        elif argument[0] != "":
            # print(argument[0]+" is not a valid parameter")
            error_message+=argument[0]+" is not a valid parameter\n"


def displayHelp():
    clear()
    print("Use the format:\nparameter1 = value, parameter2 = value to set values to parameters")

    print("The values of the following parameters can be changed:")
    print("DAYS = INTEGER\nThis sets the number of days the simulation runs for and the value should be an integer")
    print("-----------------------------------------")
    print("AGENTS = INTEGER\nThis sets the popluation of the simulation and the value should be an integer")
    print("-----------------------------------------")
    print("init_infected = INTEGER\nThis sets the initial number of infected agents in the popluation and the value should be an integer")
    print("-----------------------------------------")
    print("mask_chance = VALUE\nThis sets what portion of the popluation use masks. The value can be: ALL, MOST, HALF, FEW or NONE")
    print("school = BOOLEAN\nThis specifies if schools are open or not. The value can be: TRUE or FALSE")
    print("-----------------------------------------")
    print("child = VALUE\nThis specifies lockdown restrictions for children. The value can be: NONE, MINIMAL, MODERATE, SEVERE or TOTAL")
    print("-----------------------------------------")
    print("young = VALUE\nThis specifies lockdown restrictions for young adults. The value can be: NONE, MINIMAL, MODERATE, SEVERE or TOTAL")
    print("-----------------------------------------")
    print("adult = VALUE\nThis specifies lockdown restrictions for adults. The value can be: NONE, MINIMAL, MODERATE, SEVERE or TOTAL")
    print("-----------------------------------------")
    print("old = VALUE\nThis specifies lockdown restrictions for the elderly. The value can be: NONE, MINIMAL, MODERATE, SEVERE or TOTAL")
    print("-----------------------------------------")
    print("live_graph = BOOLEAN\nspecifies if a live graph should be used for visualisation of the simulation")

    print("=====================================")
    print("\nPress any button to go back to Settings")

    x = readchar.readkey()

    showSettings()


def showSettings() :
    clear()
    print_error_message()
    print("Number of days (days): ",DAYS)
    print("Population (agents): ",AGENTS)
    print("Initial number of infected (init_infected): ",INIT_INFECTED)
    print("------------------------------")
    print("Mask chance (mask_chance): ",MASKCHANCE)
    print("School (school): ",SETTINGS[0])
    print("------------------------------")
    print("Children lockdown settings (child): ",SETTINGS[1])
    print("Young Adult lockdown settings (young): ",SETTINGS[2])
    print("Adult lockdown settings (adult): ",SETTINGS[3])
    print("Elderly lockdown settings (old): ",SETTINGS[4])
    print("------------------------------")
    print("Live graphs: (live_graph)",LIVE_GRAPH_STATUS)
    print("==============================")

    print("\nPress 1 to go back to Main Menu")
    print("Press 2 to change settings")
    print("Press H for settings help")
    print("Press Q to exit")


    while True:
        x = readchar.readkey()
        if x == '1':
            mainMenu()
            break
        elif x == '2':
            print("Enter new settings: ")
            arguments = input()
            mapSettings(arguments)
            showSettings()
            break
        elif x.lower() == 'q':
            exit() 
        elif x.lower() == 'h':
            displayHelp()

    
    
        
def mainMenu():
    clear()
    print_error_message()
    print("press 1 to proceed with simulation")
    print("press 2 to view current settings")
    print("press Q to quit ")

    while True:
        x = readchar.readkey()
        if x == '1':
            runSingle()
            mainMenu()
        if x == '2':
            showSettings()
            break
        if x.lower() == 'q':
            exit()    


def clear():
    if os.name in ('nt','dos'):
        os.system("cls")
    elif os.name in ('linux','osx','posix'):
        os.system("clear")
    else:
        print("\n") * 120


if __name__ == '__main__':
    
    arguments = ''.join(sys.argv[1:])
    mapSettings(arguments)

    mainMenu()
    
    
    #runComplete()
