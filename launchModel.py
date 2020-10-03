import model.virusModel as vm
import visualisation.dataCollector as dc
from visualisation.visualisation import *


model = vm.VirusModel()
data_collector = dc.DataCollector()

days = 150
for day in range(1,days+1):
    print('Day '+ str(day))
    model.step()
    data_collector.print_overall_stats(model)
    data_collector.collect_daily_data(model)


# Summary of the simulation

data_collector.print_summary()
df = data_collector.total_dead_agents(model)

# Visualisation

summary = data_collector.simulation_summary()
perform_visualisation(summary, df)

