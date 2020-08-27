# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:02:22 2020

@author: Nebojsa Dubocanin
"""

# Created on Wed July 7 20:28:14 2020
# @author: Nebojsa Dubocanin
# @supervisor: Angelika Hess
# @head: Prof. Dr. Eberhard Morgenroth
# Affiliation: Eawag - Swiss Federal Institute for Aquatic Research
# Unit: Water Hub @ NEST
# Team: Process Engineering
# Purpose: Data Analysis of the experiments for Master Project


# IMPORTING THE DATA FROM THE EXPERIMENT 2
# TWO LIBRARIES WILL BE USED FOR DATA ANALYSIS, PANDAS AND MATPLOTLIB

# LOADING NECESSARY Python MODULES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# LOADING DATA and DEFINING HEADERS
avg_tcc = pd.read_csv('data/avg_tcc.txt', sep=",", 
                      names=["time", "H", "H0", "H1", "H5", "H10"])

std_tcc = pd.read_csv('data/std_tcc.txt', sep=",", 
                      names=["time", "H", "H0", "H1", "H5", "H10"])

# EXTRACTING TCC COUNTS [#/mL]
t = avg_tcc["time"]
h = avg_tcc["H"]
h0 = avg_tcc["H0"]
h1 = avg_tcc["H1"]
h5 = avg_tcc["H5"]
h10 = avg_tcc["H10"]
sh = std_tcc["H"]
sh0 = std_tcc["H0"]
sh1 = std_tcc["H1"]
sh5 = std_tcc["H5"]
sh10 = std_tcc["H10"]

port_names = np.array(["M3-RAW", "M3 A-0.5", "M3 A-1", "M3 A-5", "M3 A-10"]).T

# GROWTH CURVES
fig, ax = plt.subplots()
ax.errorbar(t, h, yerr = sh, capsize = 5,
              linestyle='dotted', linewidth = 1, 
             marker="o", markerfacecolor='black', markersize=8)
ax.errorbar(t, h0, yerr = sh0, capsize = 5,
              linestyle='dashed', linewidth = 1, 
             marker="d", markerfacecolor='black', markersize=8)
ax.errorbar(t, h1, yerr = sh1, capsize = 5,
              linestyle='dashdot', linewidth = 1, 
             marker="v", markerfacecolor='black', markersize=8)
ax.errorbar(t, h5, yerr = sh5, capsize = 5,
              linestyle='dashdot', linewidth = 1, 
             marker="p", markerfacecolor='black', markersize=8)
ax.errorbar(t, h10, yerr = sh10, capsize = 5,
              linestyle='dashdot', linewidth = 1, 
             marker="h", markerfacecolor='black', markersize=8)
ax.legend(["M3-No Acetate", "M3 0.5 [$\mu$g/mL]", "M3 1.0 [$\mu$g/mL]", "M3 5.0 [$\mu$g/mL]", "M3 10.0 [$\mu$g/mL]"], loc = "upper right")
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.xaxis.set_label_text('Time [h]', fontsize=12)
ax.yaxis.set_label_text('Cells [TCC/ml]', fontsize=12)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.savefig('figures/ex3_m3_acetate.png', bbox_inches = "tight", dpi = 110)