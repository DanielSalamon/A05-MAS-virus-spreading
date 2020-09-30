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


	plt.show()