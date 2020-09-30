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
    data_collector.collect_disease_stats_of_the_day(model)


# Summary of the simulation

summary = data_collector.simulation_summary()
print("Summary of the simulation:\n")
print(summary)
draw_disease_plot(summary)

