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
df = pd.read_csv("data_ex2.csv")

c0 = df["cell0 (#/mL)"]
c1 = df["cell1 (#/mL)"]
c2 = df["cell2 (#/mL)"]
c5 = df["cell5 (#/mL)"]
c7 = df["cell7 (#/mL)"]
c9 = df["cell9 (#/mL)"]
dc = df["delta TCC (#/mL)"]
e = df["end TCC (#/mL)"]

# specify the custom font to use
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Lucida Sans Unicode'

                                            # SAMPLING LOCATION A5 #
#################################################################################################################
a5 = np.array([nh.mean(c0[0:3]), nh.mean(c1[0:3]), nh.mean(c2[0:3]), nh.mean(c5[0:3]), nh.mean(c7[0:3]), nh.mean(c9[0:3])])
a5s = np.array([nh.std(c0[0:3]), nh.std(c1[0:3]), nh.std(c2[0:3]), nh.std(c5[0:3]), nh.std(c7[0:3]), nh.std(c9[0:3])])

                                            # SAMPLING LOCATION A4 #
#################################################################################################################
a4 = np.array([nh.mean(c0[3:6]), nh.mean(c1[3:6]), nh.mean(c2[3:6]), nh.mean(c5[3:6]), nh.mean(c7[3:6]), nh.mean(c9[3:6])])
a4s = np.array([nh.std(c0[3:6]), nh.std(c1[3:6]), nh.std(c2[3:6]), nh.std(c5[3:6]), nh.std(c7[3:6]), nh.std(c9[3:6])])

                                            # SAMPLING LOCATION A3 #
#################################################################################################################
a3 = np.array([nh.mean(c0[6:9]), nh.mean(c1[6:9]), nh.mean(c2[6:9]), nh.mean(c5[6:9]), nh.mean(c7[6:9]), nh.mean(c9[6:9])])
a3s = np.array([nh.std(c0[6:9]), nh.std(c1[6:9]), nh.std(c2[6:9]), nh.std(c5[6:9]), nh.std(c7[6:9]), nh.std(c9[6:9])])

                                            # SAMPLING LOCATION A2 #
#################################################################################################################
a2 = np.array([nh.mean(c0[9:12]), nh.mean(c1[9:12]), nh.mean(c2[9:12]), nh.mean(c5[9:12]), nh.mean(c7[9:12]), nh.mean(c9[9:12])])
a2s = np.array([nh.std(c0[9:12]), nh.std(c1[9:12]), nh.std(c2[9:12]), nh.std(c5[9:12]), nh.std(c7[9:12]), nh.std(c9[9:12])])

                                            # SAMPLING LOCATION A1 #
#################################################################################################################
a1 = np.array([nh.mean(c0[12:15]), nh.mean(c1[12:15]), nh.mean(c2[12:15]), nh.mean(c5[12:15]), nh.mean(c7[12:15]), nh.mean(c9[12:15])])
a1s = np.array([nh.std(c0[12:15]), nh.std(c1[12:15]), nh.std(c2[12:15]), nh.std(c5[12:15]), nh.std(c7[12:15]), nh.std(c9[12:15])])

                                            # SAMPLING LOCATION B5 #
#################################################################################################################
b5 = np.array([nh.mean(c0[15:18]), nh.mean(c1[15:18]), nh.mean(c2[15:18]), nh.mean(c5[15:18]), nh.mean(c7[15:18]), nh.mean(c9[15:18])])
b5s = np.array([nh.std(c0[15:18]), nh.std(c1[15:18]), nh.std(c2[15:18]), nh.std(c5[15:18]), nh.std(c7[15:18]), nh.std(c9[15:18])])

                                            # SAMPLING LOCATION B4 #
#################################################################################################################
b4 = np.array([nh.mean(c0[18:21]), nh.mean(c1[18:21]), nh.mean(c2[18:21]), nh.mean(c5[18:21]), nh.mean(c7[18:21]), nh.mean(c9[18:21])])
b4s = np.array([nh.std(c0[18:21]), nh.std(c1[18:21]), nh.std(c2[18:21]), nh.std(c5[18:21]), nh.std(c7[18:21]), nh.std(c9[18:21])])

                                            # SAMPLING LOCATION B3 #
#################################################################################################################
b3 = np.array([nh.mean(c0[21:24]), nh.mean(c1[21:24]), nh.mean(c2[21:24]), nh.mean(c5[21:24]), nh.mean(c7[21:24]), nh.mean(c9[21:24])])
b3s = np.array([nh.std(c0[21:24]), nh.std(c1[21:24]), nh.std(c2[21:24]), nh.std(c5[21:24]), nh.std(c7[21:24]), nh.std(c9[21:24])])

                                            # SAMPLING LOCATION B2 #
#################################################################################################################
b2 = np.array([nh.mean(c0[24:27]), nh.mean(c1[24:27]), nh.mean(c2[24:27]), nh.mean(c5[24:27]), nh.mean(c7[24:27]), nh.mean(c9[24:27])])
b2s = np.array([nh.std(c0[24:27]), nh.std(c1[24:27]), nh.std(c2[24:27]), nh.std(c5[24:27]), nh.std(c7[24:27]), nh.std(c9[24:27])])

                                         # SAMPLING LOCATION B1 #
#################################################################################################################
b1 = np.array([nh.mean(c0[27:30]), nh.mean(c1[27:30]), nh.mean(c2[27:30]), nh.mean(c5[27:30]), nh.mean(c7[27:30]), nh.mean(c9[27:30])])
b1s = np.array([nh.std(c0[27:30]), nh.std(c1[27:30]), nh.std(c2[27:30]), nh.std(c5[27:30]), nh.std(c7[27:30]), nh.std(c9[27:30])])

                                        # VECTORS FOR COMPARISON PLOTS #
#################################################################################################################
tcc_m2 = np.array([nh.mean(dc[0:3]), nh.mean(dc[3:6]), nh.mean(dc[6:9]), nh.mean(dc[9:12]), nh.mean(dc[12:15])])
tcc_m2s = np.array([nh.std(dc[0:3]), nh.std(dc[3:6]), nh.std(dc[6:9]), nh.std(dc[9:12]), nh.std(dc[12:15])])
ini_m2 = np.array([a5[0], a4[0], a3[0], a2[0], a1[0]])
ini_m2s = np.array([a5s[0], a4s[0], a3s[0], a2s[0], a1s[0]])
end_m2 = np.array([nh.mean(e[0:3]), nh.mean(e[3:6]), nh.mean(e[6:9]), nh.mean(e[9:12]), nh.mean(e[12:15])])
end_m2s = np.array([nh.std(e[0:3]), nh.std(e[3:6]), nh.std(e[6:9]), nh.std(e[9:12]), nh.std(e[12:15])])

tcc_m3 = np.array([nh.mean(dc[15:18]), nh.mean(dc[18:21]), nh.mean(dc[21:24]), nh.mean(dc[24:27]), nh.mean(dc[27:30])])
tcc_m3s = np.array([nh.std(dc[15:18]), nh.std(dc[18:21]), nh.std(dc[21:24]), nh.std(dc[24:27]), nh.std(dc[27:30])])
ini_m3 = np.array([b5[0], b4[0], b3[0], b2[0], b1[0]])
ini_m3s = np.array([b5s[0], b4s[0], b3s[0], b2s[0], b1s[0]])
end_m3 = np.array([nh.mean(e[15:18]), nh.mean(e[18:21]), nh.mean(e[21:24]), nh.mean(e[24:27]), nh.mean(e[27:30])])
end_m3s = np.array([nh.std(e[15:18]), nh.std(e[18:21]), nh.std(e[21:24]), nh.std(e[24:27]), nh.std(e[27:30])])

                                    # STACKED BAR PLOT: INITIAL #TCC + INCREASE OVER TIME FOR M2 #
###############################################################################################################################
#dif_vector = [int(i) for i in tcc_m2s]
#init_vector = [int(i) for i in init_vector]
ini = np.array([ini_m2[0], ini_m2[1], ini_m2[2], ini_m3[0], ini_m3[1]])
tcc = np.array([tcc_m2[0], tcc_m2[1], tcc_m2[2], tcc_m3[0], tcc_m3[1]])
tccs = np.array([tcc_m2s[0], tcc_m2s[1], tcc_m2s[2], tcc_m3s[0], ini_m3[1]])
     
N = 5
ind = np.arange(N)  # the x locations for the groups/bars
width = 0.35        # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
p1 = plt.bar(ind, ini, width)
p2 = plt.bar(ind, tcc, width, yerr = tccs, capsize = 5, bottom=ini)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.ylabel('Cells [TCC/mL]', fontsize=12)
plt.xlabel('[Sample Names]', fontsize=12)
plt.xticks(ind, ('$M2_{1:10000}$', '$M2_{1:1000}$', '$M2_{1:100}$', '$M3_{1:10000}$', '$M3_{1:1000}$'))
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.legend((p1[0], p2[0]), ('Initial TCC', "$\Delta$ TCC"))

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

plt.savefig('figures/ex2_ini_diff.png', bbox_inches = "tight", dpi = 110)

                    # COMPARISON OF SAMPLES WITHOUT GROWTH #
###############################################################################
x1 = np.array([ini_m2[3], ini_m2[4], ini_m3[2], ini_m3[3], ini_m3[4]])
x1s = np.array([ini_m2s[3], ini_m2s[4], ini_m3s[2], ini_m3s[3], ini_m3s[4]])
z1 = np.array([tcc_m2[3], tcc_m2[4], tcc_m3[2], tcc_m3[3], tcc_m3[4]])*(-1)
z1s = np.array([tcc_m2s[3], tcc_m2s[4], tcc_m3s[2], tcc_m3s[3], tcc_m3s[4]])
y1 = np.array([end_m2[3], end_m2[4], end_m3[2], end_m3[3], end_m3[4]])

indices = range(len(x1))              # number of bars
width = np.min(np.diff(indices))/2.5    # Calculate optimal width for 2 (no space between bars)

fig = plt.figure()
ax = fig.add_subplot()

ax.bar(indices-width/2, x1, width, yerr = x1s, capsize = 5, label = "Initial TCC")
ax.bar(indices+width/2, z1, width, yerr = z1s, capsize = 5, bottom = y1, label = "$\Delta$ TCC")
ax.bar(indices+width/2, y1, width, label = "End TCC")
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.xticks(ind, ("M2 1:10", "M2 1:1", "M3 1:100", "M3 1:10", "M3 1:1"))
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc="upper right")
plt.ylabel('Cells [TCC/mL]', fontsize=12)
plt.xlabel('[Sample Names]', fontsize=12)
plt.savefig('figures/ex2_ini_end.png', bbox_inches = "tight", dpi = 110)

                    # COMPARISON OF SAMPLES WITHOUT GROWTH #
###############################################################################
f = pd.read_csv("data_ex2a.csv")
f = f.sort_values("init RC (ug-TOC/cell)")
x = f["init RC (ug-TOC/cell)"]
ym2 = f["M2Y (#/ug)"]
ym2[ ym2==0 ] = np.nan
ym3 = f["M3Y (#/ug)"]
ym3[ ym3==0 ] = np.nan

fig = plt.figure()
ax = fig.add_subplot()

plt.scatter(x, ym2, label="Yields M2")
plt.scatter(x, ym3, label="Yields M3")
plt.xscale("log")
plt.legend(loc="upper left")
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.xlabel("R/C [$\mu$gTOC/cell]", fontsize=12)
plt.ylabel("Y [#/$\mu$g]", fontsize=12)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0e'))
plt.savefig('figures/Y_vs_RC_ex2.png', bbox_inches = "tight", dpi = 110)

                                            # SAVE THE VECTORS FILES FOR GROWTH CURVE PLOTS #
###########################################################################################################################
t = np.array([0, 24, 48, 120, 168, 216])
avg = np.vstack((t, 
                    a5.T, a4.T, a3.T, a2.T, a1.T,
                    b5.T, b4.T, b3.T, b2.T, b1.T)) # vertical stack
avg = avg.T # transpose data
np.savetxt('data/avg_tcc.txt', avg, delimiter=',')

# SAVE THE VECTORS WITH STANDARD DEVIATION OF EACH TRIPLICATE
std = np.vstack((t,
                    a5s.T, a4s.T, a3s.T, a2s.T, a1s.T,
                    b5s.T, b4s.T, b3s.T, b2s.T, b1s.T)) # vertical stack
std = std.T             # transpose data
np.savetxt('data/std_tcc.txt',std,delimiter=',')