import model.virusModel as vm
import visualisation.dataCollector as dc
from visualisation.visualisation import *
from multiprocessing import Process


def MainProgram(days,live_graph=True):
	model = vm.VirusModel()
	data_collector = dc.DataCollector()

	for day in range(1,days+1):
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

	number_of_days = 365
	live_graph_status = True


	if live_graph_status :
	    f = open("visualisation\\visual_data.txt", "w")
	    f.close()



	    p = Process(target=live_animation)
	    p.start()
	    MainProgram(number_of_days,live_graph=live_graph_status)
	    p.join()

	else:			
		MainProgram(number_of_days,live_graph=False)

