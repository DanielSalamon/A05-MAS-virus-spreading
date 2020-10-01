import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


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

    