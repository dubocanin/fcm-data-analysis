# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:15:46 2020

@author: Nebojsa Dubocanin
"""


# LOADING NECESSARY Python MODULES
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# LOADING DATA and DEFINING HEADERS

avg_tcc = pd.read_csv('data/avg_tcc.txt', sep=",", 
                      names=["time", "M2 1:10000", "M2 1:1000", "M2 1:100", "M2 1:10", "M2 1:1",
                             "M3 1:10000", "M3 1:1000", "M3 1:100", "M3 1:10", "M3 1:1"])
std_tcc = pd.read_csv('data/std_tcc.txt', sep=",",
                      names=["time", "M2 1:10000", "M2 1:1000", "M2 1:100", "M2 1:10", "M2 1:1",
                             "M3 1:10000", "M3 1:1000", "M3 1:100", "M3 1:10", "M3 1:1"])

# TIME VECTOR
t = avg_tcc["time"]

# DATA M2 1:1
M2_A1 = avg_tcc["M2 1:1"]
M2_A1_std = std_tcc["M2 1:1"]

# DATA M2 1:10
M2_A2 = avg_tcc["M2 1:10"]
M2_A2_std = std_tcc["M2 1:10"]

# DATA M2 1:100
M2_A3 = avg_tcc["M2 1:100"]
M2_A3_std = std_tcc["M2 1:100"]

# DATA M2 1:1000
M2_A4 = avg_tcc["M2 1:1000"]
M2_A4_std = std_tcc["M2 1:1000"]

# DATA M2 1:10000
M2_A5 = avg_tcc["M2 1:10000"]
M2_A5_std = std_tcc["M2 1:10000"]

############################ M2 GROWTH PLOT - 9 DAYS ##########################
# GROWTH
fig, ax = plt.subplots()
ax.errorbar(t, M2_A3, yerr = M2_A3_std, capsize = 5,
              linestyle='dotted', linewidth = 1, 
             marker='o', markerfacecolor='black', markersize=7)
ax.errorbar(t, M2_A4, yerr = M2_A4_std, capsize = 5,
              linestyle='dashed', linewidth = 1, 
             marker='^', markerfacecolor='black', markersize=7)
ax.errorbar(t, M2_A5, yerr = M2_A5_std, capsize = 5,
              linestyle='dashdot', linewidth = 1, 
             marker='s', markerfacecolor='black', markersize=7)
ax.legend(['M2 1:100', 'M2 1:1000', 'M2 1:10000'], loc = "upper left")
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.xaxis.set_label_text('Time [h]', fontsize=12)
ax.yaxis.set_label_text('Cells [TCC/ml]', fontsize=12)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.savefig('figures/ex2_m2_growth.png', bbox_inches = "tight", dpi = 110)

# NO GROWTH
fig, ax = plt.subplots()
ax.errorbar(t, M2_A1, yerr = M2_A1_std, capsize = 5,
              linestyle='dotted', linewidth = 1, 
              marker='o', markerfacecolor='black', markersize=7)
ax.errorbar(t, M2_A2, yerr = M2_A2_std, capsize = 5,
              linestyle='dashdot', linewidth = 1, 
              marker='s', markerfacecolor='black', markersize=7)
ax.legend(['M2 1:1','M2 1:10'], loc = "upper right")
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.xaxis.set_label_text('Time [h]', fontsize=12)
ax.yaxis.set_label_text('Cells [TCC/ml]', fontsize=12)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.savefig('figures/ex2_m2_nogrowth.png', bbox_inches = "tight", dpi = 110)

# DATA M3 1:1
M3_B1 = avg_tcc["M3 1:1"]
M3_B1_std = std_tcc["M3 1:1"]

# DATA M3 1:10
M3_B2 = avg_tcc["M3 1:10"]
M3_B2_std = std_tcc["M3 1:10"]

# DATA M3 1:100
M3_B3 = avg_tcc["M3 1:100"]
M3_B3_std = std_tcc["M3 1:100"]

# DATA M3 1:1000
M3_B4 = avg_tcc["M3 1:1000"]
M3_B4_std = std_tcc["M3 1:1000"]

# DATA M3 1:10000
M3_B5 = avg_tcc["M3 1:10000"]
M3_B5_std = std_tcc["M3 1:10000"]

############################ M3 GROWTH PLOT - 9 DAYS ##########################
# GROWTH
fig, ax = plt.subplots()
ax.errorbar(t, M3_B3, yerr = M3_B3_std, capsize = 5,
             linestyle='dotted', linewidth = 1, 
             marker='o', markerfacecolor='black', markersize=7)
ax.errorbar(t, M3_B4, yerr = M3_B4_std, capsize = 5,
             linestyle='dashed', linewidth = 1, 
             marker='^', markerfacecolor='black', markersize=7)
ax.errorbar(t, M3_B5, yerr = M3_B5_std, capsize = 5,
             linestyle='dashdot', linewidth = 1, 
             marker='s', markerfacecolor='black', markersize=7)
ax.legend(['M3 1:100', 'M3 1:1000', 'M3 1:10000'], loc = "lower right")
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.xaxis.set_label_text('Time [h]', fontsize=12)
ax.yaxis.set_label_text('Cells [TCC/ml]', fontsize=12)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.savefig('figures/ex2_m3_growth.png', bbox_inches = "tight", dpi = 110)

# NO GROWTH
fig, ax = plt.subplots()
ax.errorbar(t, M3_B1, yerr = M3_B1_std, capsize = 5,
              linestyle='dotted', linewidth = 1, 
              marker='o', markerfacecolor='black', markersize=7)
ax.errorbar(t, M3_B2, yerr = M3_B2_std, capsize = 5,
              linestyle='dashdot', linewidth = 1, 
              marker='s', markerfacecolor='black', markersize=7)
ax.legend(['M3 1:1','M3 1:10'], loc = "upper right")
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.xaxis.set_label_text('Time [h]', fontsize=12)
ax.yaxis.set_label_text('Cells [TCC/ml]', fontsize=12)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.savefig('figures/ex2_m3_nogrowth.png', bbox_inches = "tight", dpi = 110)