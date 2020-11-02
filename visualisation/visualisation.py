import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd 

# draw plots

def draw_disease_plot(data_frame):

	styles = ['green','orange','red', 'black', 'lightblue']
	linewidths = [1, 1, 1, 1, 1]
	fig, ax = plt.subplots()
	for col, style, lw in zip(data_frame.columns, styles, linewidths):
	    data_frame[col].plot(style=style, lw=lw, ax=ax)
	    plt.xlabel("Day")
	    plt.ylabel("Number of agents")
	    plt.legend(['susceptible', 'exposed', 'infected', 'removed', 'recovered'])
	    plt.title("Population statistics over whole simulation")


	plt.savefig("visualisation/plots/Overall.png")
	plt.close(fig)



def draw_plot_by_group_age(data_frame, age_group):


	styles = ['green','orange','red', 'black', 'lightblue']
	linewidths = [1, 1, 1, 1, 1]
	fig, ax = plt.subplots()
	for col, style, lw in zip(data_frame.columns, styles, linewidths):
	    data_frame[col].plot(style=style, lw=lw, ax=ax)
	    plt.xlabel("Day")
	    plt.ylabel("Number of agents")
	    plt.legend(['susceptible', 'exposed', 'infected', 'removed', 'recovered'])
	    plt.title("Disease statistics for age group: " + age_group)

	plt.savefig("visualisation/plots/" + age_group + ".png")
	plt.close(fig)



def draw_plots_by_age_groups(data_frames, dead_agents, recovered_agents):

	img_labels = ["Overall", "Child", "Young", "Adult", "Old", "Deaths"]

	for i in range(1,5):
		draw_plot_by_group_age(data_frames[i], img_labels[i])

	draw_disease_plot(data_frames[0])
	visualize_dead_and_recovered_agents(dead_agents, recovered_agents)
	
	fig=plt.figure(figsize=(15, 10))
	columns = 2
	rows = 3
	for i in range(1, columns*rows +1):
	    img = plt.imread("visualisation/plots/" + img_labels[i-1] + ".png")
	    a = fig.add_subplot(rows, columns, i)
	    img_plot = plt.imshow(img)
	plt.show()


def visualize_dead_and_recovered_agents(dead, recovered):



	labels = ['Children', 'Young', 'Adults', 'Olds']
	deaths = [dead[0][0], dead[1][0], dead[2][0], dead[3][0]]
	#rec = [recovered[0][0], recovered[1][0], recovered[2][0], recovered[3][0]]

	x = np.arange(len(labels))  # the label locations
	width = 0.35  # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(x - width/2, deaths, width, label='Died')
	#rects2 = ax.bar(x + width/2, rec, width, label='Recovered')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Numer of agents')
	ax.set_title('Dead agents by age group')
	ax.set_xticks(x)
	ax.set_xticklabels(labels)
	ax.legend()


	def autolabel(rects):
	    """Attach a text label above each bar in *rects*, displaying its height."""
	    for rect in rects:
	        height = rect.get_height()
	        ax.annotate('{}'.format(height),
	                    xy=(rect.get_x() + rect.get_width() / 2, height),
	                    xytext=(0, 3),  # 3 points vertical offset
	                    textcoords="offset points",
	                    ha='center', va='bottom')


	autolabel(rects1)
	#autolabel(rects2)

	fig.tight_layout()

	plt.savefig("visualisation/plots/Deaths.png")
	plt.close(fig)

def perform_visualisation(summary, dead_agents, recovered_agents):
	#draw_disease_plot(summary[0])
	draw_plots_by_age_groups(summary, dead_agents, recovered_agents)
	#visualize_dead_agents(df)

fig = plt.figure()
age_axis = fig.add_subplot(2,1,1)
condition_axis = fig.add_subplot(2,1,2)
axis_limit = 0
# young_axis = fig.add_subplot(1,1,1)
# adult_axis = fig.add_subplot(1,1,1)
# old_axis = fig.add_subplot(1,1,1)
################################################

def animate(i):
	graph_data = open("visualisation/visual_data.txt",'r').read()
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
	recovered_axis_data = []
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
			recovered_axis_data.append(int(line[8]))

	age_axis.clear()
	condition_axis.clear()
	global axis_limit
	age_axis.set_xlim([0,axis_limit])
	condition_axis.set_xlim([0,axis_limit])
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
	condition_axis.plot(recovered_axis_data,label='recovered')
	condition_axis.legend(loc='upper left',prop={'size':6})



def live_animation(axis_length):
	global axis_limit
	axis_limit = axis_length
	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()