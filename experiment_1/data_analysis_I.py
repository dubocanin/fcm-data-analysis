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

#Storing data into data frames
df = pd.read_csv("data.csv")

c0 = df["cell0 (#/mL)"]
c2 = df["cell2 (#/mL)"]
c5 = df["cell5 (#/mL)"]
dc = df["delta TCC (#/mL)"]
y = df["Y (#/ug)"]

# Creating vectors for plots
days = ["Day 0", "Day 2", "Day 5"] # this will be on the X-AXIS

# specify the custom font to use
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Lucida Sans Unicode'

                            # SAMPLING LOCATION M2 #
###############################################################################
m2 = [nh.mean(c0[0:3]), nh.mean(c2[0:3]), nh.mean(c5[0:3])]
m2s = [nh.std(c0[0:3]), nh.std(c2[0:3]), nh.std(c5[0:3])]

m2c = nh.mean(dc[0:3])
m2cs = nh.std(dc[0:3])

m2y = nh.mean(y[0:3])
m2ys = nh.std(y[0:3])
                            # SAMPLING LOCATION W1 #
###############################################################################
w1 = [nh.mean(c0[3:6]), nh.mean(c2[3:6]), nh.mean(c5[3:6])]
w1s = [nh.std(c0[3:6]), nh.std(c2[3:6]), nh.std(c5[3:6])]

w1c = nh.mean(dc[3:6])
w1cs = nh.std(dc[3:6])

w1y = nh.mean(y[3:6])
w1ys = nh.std(y[3:6])
                            # SAMPLING LOCATION W2 #
###############################################################################
w2 = [nh.mean(c0[6:9]), nh.mean(c2[6:9]), nh.mean(c5[6:9])]
w2s = [nh.std(c0[6:9]), nh.std(c2[6:9]), nh.std(c5[6:9])]

w2c = nh.mean(dc[6:9])
w2cs = nh.std(dc[6:9])

w2y = nh.mean(y[6:9])
w2ys = nh.std(y[6:9])
                            # SAMPLING LOCATION W3 #
###############################################################################
w3 = [nh.mean(c0[9:12]), nh.mean(c2[9:12]), nh.mean(c5[9:12])]
w3s = [nh.std(c0[9:12]), nh.std(c2[9:12]), nh.std(c5[9:12])]

w3c = nh.mean(dc[9:12])
w3cs = nh.std(dc[9:12])

w3y = nh.mean(y[9:12])
w3ys = nh.std(y[9:12])
                            # SAMPLING LOCATION M3 #
###############################################################################
m3 = [nh.mean(c0[12:15]), nh.mean(c2[12:15]), nh.mean(c5[12:15])]
m3s = [nh.std(c0[12:15]), nh.std(c2[12:15]), nh.std(c5[12:15])]

m3c = nh.mean(dc[12:15])
m3cs = nh.std(dc[12:15])

m3y = nh.mean(y[12:15])
m3ys = nh.std(y[12:15])

                # PLOT M3 - BACTERIA GROWTH CURVE #
###############################################################################
# plotting the data
fig, ax = plt.subplots()

ax.errorbar(days, m2, yerr = m2s, capsize = 5,
             linestyle='dashed', linewidth = 1, 
             marker='s', markerfacecolor='black', markersize=7)
ax.errorbar(days, w1, yerr = w1s, capsize = 5,
             linestyle='dashed', linewidth = 1, 
             marker='p', markerfacecolor='black', markersize=7)
ax.errorbar(days, w2, yerr = w2s, capsize = 5,
             linestyle='dashed', linewidth = 1, 
             marker='^', markerfacecolor='black', markersize=7)
ax.errorbar(days, w3, yerr = w3s, capsize = 5,
             linestyle='dashed', linewidth = 1, 
             marker='v', markerfacecolor='black', markersize=7)
ax.errorbar(days, m3, yerr = m3s, capsize = 5,
             linestyle='dashed', linewidth = 1, 
             marker='h', markerfacecolor='black', markersize=7)

ax.legend(['M2','W1','W2','W3','M3'])
ax.xaxis.set_label_text('Time [Days]', fontsize=12)
ax.yaxis.set_label_text('Cells [TCC/mL]', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))

plt.savefig('figures/ex1_growth.png', bbox_inches = "tight", dpi = 110)

            # STACKED BAR PLOT: INITIAL #TCC + INCREASE OVER TIME #
###############################################################################
dif_vector = [m2c, w1c, w2c, w3c, m3c]
# dif_vector = [int(i) for i in dif_vector]
dif_std = [m2cs, w1cs, w2cs, w3cs, m3cs]
init_vector = [m2[0], w1[0], w2[0], w3[0], m3[0]]        
# init_vector = [int(i) for i in init_vector]     

# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
# autolabel(p1)
# autolabel(p2)

# plt.savefig('figures/ex1_ini_diff.png', bbox_inches = "tight", dpi = 110)

                    # COMPARISON WITH CECILES RESILTS #
###############################################################################
nash = [m2[2], w1[2], w2[2], w3[2], m3[2]]
nash_std = np.array([m2s[2], w1s[2], w2s[2], w3s[2], m3s[2]])

cecile = np.array([621333.333333333, 417250, 357250, 377500, 238083.333333333])
ports = np.array(["M2", "W1", "W2", "W3", "M3"])

indices = range(len(dif_vector))              # number of bars
width = np.min(np.diff(indices))/2.5    # Calculate optimal width for 2 (no space between bars)

fig = plt.figure()
ax = fig.add_subplot()

ax.bar(indices-width/2., dif_vector, width, yerr = dif_std, capsize = 5, 
       bottom = init_vector, label = "$\Delta$ TCC")
ax.bar(indices-width/2., init_vector, width, label = "Initial TCC")
ax.bar(indices+width/2., cecile, width, label = "Bettex [2019]")
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.xticks(indices, ('M2', 'W1', 'W2', 'W3', 'M3'))
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc="upper right")
plt.ylabel('Cells [TCC/mL]', fontsize=12)
plt.xlabel('[Sampling Locations]', fontsize=12)
plt.savefig('figures/ex1_comparison.png', bbox_inches = "tight", dpi = 110)