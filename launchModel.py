import model.virusModel as vm
import visualisation.dataCollector as dc
from visualisation.visualisation import *
from multiprocessing import Process

DAYS = 50 # desired days model will run

AGENTS = 1000 # desired agents model will have

def MainProgram(live_graph=True):
	model = vm.VirusModel(AGENTS)
	data_collector = dc.DataCollector()

	for day in range(1,DAYS+2):
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



if __name__ == '__main__':
	live_graph_status = True

	if live_graph_status :
	    f = open("visualisation\\visual_data.txt", "w")
	    f.close()

	    p = Process(target=live_animation)
	    p.start()
	    MainProgram(live_graph=live_graph_status)
	    p.join()

	else:			
		MainProgram(live_graph=False)

