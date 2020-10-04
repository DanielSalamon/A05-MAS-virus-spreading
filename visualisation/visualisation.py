import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd 

# draw plots

def draw_disease_plot(data_frame):

	styles = ['green','orange','red', 'black']
	linewidths = [1, 1, 1, 1]
	fig, ax = plt.subplots()
	for col, style, lw in zip(data_frame.columns, styles, linewidths):
	    data_frame[col].plot(style=style, lw=lw, ax=ax)
	    plt.xlabel("Day")
	    plt.ylabel("Number of agents")
	    plt.legend(['susceptible', 'exposed', 'infected', 'removed'])
	    plt.title("Population statistics over whole simulation")


	plt.show()



def draw_plot_by_group_age(data_frame, age_group):


	styles = ['green','orange','red', 'black']
	linewidths = [1, 1, 1, 1]
	fig, ax = plt.subplots()
	for col, style, lw in zip(data_frame.columns, styles, linewidths):
	    data_frame[col].plot(style=style, lw=lw, ax=ax)
	    plt.xlabel("Day")
	    plt.ylabel("Number of agents")
	    plt.legend(['susceptible', 'exposed', 'infected', 'removed'])
	    plt.title("Disease statistics for age group: " + age_group)


	plt.show()



def draw_plots_by_age_groups(data_frames):

	age_groups = ["Child", "Young", "Adult", "Old"]

	for i in range(4):
		draw_plot_by_group_age(data_frames[i], age_groups[i])


def visualize_dead_agents(data_frame):

	data_frame.plot(kind="bar")
	plt.ylabel("Number of dead agents")
	plt.title("Dead agents per age group")
	plt.show()

def perform_visualisation(summary, df):
	draw_disease_plot(summary[0])
	draw_plots_by_age_groups(summary[1:])
	visualize_dead_agents(df)

fig = plt.figure()
age_axis = fig.add_subplot(2,1,1)
condition_axis = fig.add_subplot(2,1,2)
# young_axis = fig.add_subplot(1,1,1)
# adult_axis = fig.add_subplot(1,1,1)
# old_axis = fig.add_subplot(1,1,1)
################################################

def animate(i):
	graph_data = open("visualisation\\visual_data.txt",'r').read()
	lines = graph_data.split('\n')
	children_axis_data = []
	young_axis_data = []
	adult_axis_data = []
	old_axis_data = []
	#####################for second figure
	susceptible_axis_data = []
	exposed_axis_data = []
	infected_axis_data = []
	removed_axis_data = []
	###################################

	# print(lines)
	count = 0
	x_axis = []
	for line in lines:
		if line != '':
			count+=1
			x_axis.append(count)
			line = line.split(',')

			children_axis_data.append(int(line[0]))
			young_axis_data.append(int(line[1]))
			adult_axis_data.append(int(line[2]))
			old_axis_data.append(int(line[3]))

			susceptible_axis_data.append(int(line[4]))
			exposed_axis_data.append(int(line[5]))
			infected_axis_data.append(int(line[6]))
			removed_axis_data.append(int(line[7]))

	age_axis.clear()
	condition_axis.clear()
	age_axis.set_title('Live graph of Agents')
	age_axis.set_ylabel('Number of Agents')
	condition_axis.set_ylabel('Number of Agents')
	condition_axis.set_xlabel('Day')
	# young_axis.clear()
	# adult_axis.clear()
	# old_axis.clear()
	# xs = 
	age_axis.plot(children_axis_data,label='Children')
	age_axis.plot(young_axis_data,label='young')
	age_axis.plot(adult_axis_data,label='adult')
	age_axis.plot(old_axis_data,label='old')
	age_axis.legend(loc='upper left',prop={'size': 6})


	condition_axis.plot(susceptible_axis_data,label='susceptible')
	condition_axis.plot(exposed_axis_data,label='exposed')
	condition_axis.plot(infected_axis_data,label='infected')
	condition_axis.plot(removed_axis_data,label='removed')
	condition_axis.legend(loc='upper left',prop={'size':6})



def live_animation():

	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()