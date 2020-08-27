# -*- coding: utf-8 -*-

# Created on Wed April 5 20:28:14 2020
# @author: Nebojsa Dubocanin
# @supervisor: Angelika Hess
# @head: Prof. Dr. Eberhard Morgenroth
# Affiliation: Eawag - Swiss Federal Institute for Aquatic Research
# Unit: Water Hub @ NEST
# Team: Process Engineering
# Purpose: Data Analysis of the experiments for Master Project


# IMPORTING THE DATA FROM THE PRELIMINARY EXPERIMENT
# TWO LIBRARIES WILL BE USED FOR DATA ANALYSIS, PANDAS AND MATPLOTLIB
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
# Module for computing basic statistics
import stats as nh

# Loading data
d1 = pd.read_csv("data.csv")
d2 = pd.read_csv("data2.csv")

c0 = d1["cell0 (#/mL)"]
c2 = d1["cell2 (#/mL)"]
c5 = d1["cell5 (#/mL)"]
c7 = d1["cell7 (#/mL)"]

                                    # SAMPLING LOCATION H #
###############################################################################################
m2 = np.array([nh.mean(c0[15:18]), nh.mean(c2[15:18]), nh.mean(c5[15:18]), nh.mean(c7[15:18])])
m2s = np.array([nh.std(c0[15:18]), nh.std(c2[15:18]), nh.std(c5[15:18]), nh.std(c7[15:18])])
                                    # SAMPLING LOCATION H0 #
###############################################################################################
w1 = np.array([nh.mean(c0[18:21]), nh.mean(c2[18:21]), nh.mean(c5[18:21]), nh.mean(c7[18:21])])
w1s = np.array([nh.std(c0[18:21]), nh.std(c2[18:21]), nh.std(c5[18:21]), nh.std(c7[18:21])])
                                    # SAMPLING LOCATION H1 #
###############################################################################################
w2 = np.array([nh.mean(c0[21:24]), nh.mean(c2[21:24]), nh.mean(c5[21:24]), nh.mean(c7[21:24])])
w2s = np.array([nh.std(c0[21:24]), nh.std(c2[21:24]), nh.std(c5[21:24]), nh.std(c7[21:24])])
                                    # SAMPLING LOCATION H5 #
###############################################################################################
w3 = np.array([nh.mean(c0[24:27]), nh.mean(c2[24:27]), nh.mean(c5[24:27]), nh.mean(c7[24:27])])
w3s = np.array([nh.std(c0[24:27]), nh.std(c2[24:27]), nh.std(c5[24:27]), nh.std(c7[24:27])])
                                    # SAMPLING LOCATION H10 #
###############################################################################################
m3 = np.array([nh.mean(c0[27:30]), nh.mean(c2[27:30]), nh.mean(c5[27:30]), nh.mean(c7[27:30])])
m3s = np.array([nh.std(c0[27:30]), nh.std(c2[27:30]), nh.std(c5[27:30]), nh.std(c7[27:30])])

                        # SAVE THE VECTORS FILES FOR GROWTH CURVE PLOTS #
###############################################################################################
t = np.array([0, 48, 120, 168])
avg = np.vstack((t, 
                    m2.T, w1.T, w2.T, w3.T, m3.T)) # vertical stack
avg = avg.T # transpose data
np.savetxt('data/avg_tcc.txt', avg, delimiter=',')

# SAVE THE VECTORS WITH STANDARD DEVIATION OF EACH TRIPLICATE
std = np.vstack((t,
                    m2s.T, w1s.T, w2s.T, w3s.T, m3s.T)) # vertical stack
std = std.T             # transpose data
np.savetxt('data/std_tcc.txt',std,delimiter=',')

"""TCC plots for M23 and M32 - comparison with the data from other experiments"""
def svestenik(lst, n):
    output = []
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        p = lst[i:i+n]
        output.append(p)
    return output

tcc = svestenik(d2["delta TCC (#/mL)"], 3)
avg_tcc = np.mean(tcc, axis=1)
std_tcc = np.std(tcc, axis=1)
ini = svestenik(d2["cell0 (#/mL)"], 3)
avg_ini = np.mean(ini, axis=1)
std_ini = np.std(ini, axis=1)

""""Here we have our bars"""
N = 4
ind = np.arange(N)  # the x locations for the groups/bars
width = 0.35        # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
p1 = plt.bar(ind, avg_ini[0:4], width)
p2 = plt.bar(ind, avg_tcc[0:4], width, yerr = std_tcc[0:4], capsize = 5, bottom=avg_ini[0:4])
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.ylabel('Cells [TCC/mL]', fontsize=12)
plt.xlabel('[Sample Names]', fontsize=12)
plt.xticks(ind, ("M23", "M2-Exp.3", "M2-Exp.2", "M2-Exp.1"))
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.legend((p1[0], p2[0]), ('Initial TCC', "$\Delta$ TCC"), loc="upper right")
plt.savefig('figures/tcc_m23_ex3.png', bbox_inches = "tight", dpi = 110)

# ANOTHER, BRING IT
N = 4
ind = np.arange(N)  # the x locations for the groups/bars
width = 0.35        # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
p1 = plt.bar(ind, avg_ini[4:8], width)
p2 = plt.bar(ind, avg_tcc[4:8], width, yerr = std_tcc[4:8], capsize = 5, bottom=avg_ini[4:8])
plt.ylabel('Cells [TCC/mL]', fontsize=12)
plt.xlabel('[Sample Names]', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.xticks(ind, ("M32", "M3-Exp.3", "M3-Exp.2", "M3-Exp.1"))
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.legend((p1[0], p2[0]), ('Initial TCC', "$\Delta$ TCC"), loc="upper right")
plt.savefig('figures/tcc_m32_ex3.png', bbox_inches = "tight", dpi = 110)