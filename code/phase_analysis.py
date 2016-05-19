"""
Create a plot of the susceptibility for phase analysis
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle

########################################################################################################################

id = str(1905161638)  # id of the results to use for analysis

########################################################################################################################

f = open('results/results_' + id + '.pkl', 'rb')
results = pickle.load(f)

# show susceptibility plot
# plt.scatter(results['suscept_arr'], results['suscept_arr'])
plt.plot(results['t_arr'], pow(results['suscept_arr'], results['t_arr']) / results['N_points'])
# plt.plot(results['t_arr'], results['suscept_arr'], linestyle="",marker="o")