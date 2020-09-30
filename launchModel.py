import model.virusModel as vm
import visualisation.dataCollector as dc
from visualisation.visualisation import draw_disease_plot


model = vm.VirusModel()
data_collector = dc.DataCollector()

days = 7
for day in range(1,days+1):
    print('Day '+ str(day))
    model.step()
    data_collector.print_overall_stats(model)
    data_collector.collect_daily_data(model)


# Summary of the simulation

data_collector.print_summary()

# Visualisation
summary = data_collector.simulation_summary()
draw_disease_plot(summary[0])

