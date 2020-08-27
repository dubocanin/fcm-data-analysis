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

                        # LOADING NECESSARY Python MODULES #
###############################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from scipy.optimize import curve_fit

                            # LOADING DATA #
###############################################################################
a = pd.read_csv("aggregated.csv")
a = a.sort_values("RC (ugTOC/cell)")

                            # PREPARING DATA FOR PLOTTING #
###############################################################################
x = a["RC (ugTOC/cell)"]

y2 = a["YM2 (#/ug)"]
y2[y2==0] = np.nan
y3 = a["YM3 (#/ug)"]
y3[y3==0] = np.nan
tcc2 = a["TCCM2 (#/mL)"]
tcc2[tcc2==0] = np.nan
tcc3 = a["TCCM3 (#/mL)"]
tcc3[tcc3==0] = np.nan

                # Y vs RC including results from all experiments #
###############################################################################
fig = plt.figure()
ax = fig.add_subplot()

plt.scatter(x, y2, label="Yields M2")
plt.scatter(x, y3, label="Yields M3")
plt.xscale("log")
plt.legend(loc="upper left")
plt.xlabel("R/C [$\mu$gTOC/cell]", fontsize=12)
plt.ylabel("Y [#/$\mu$g]", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0e'))
plt.savefig('figures/agg_yrc.png', bbox_inches = "tight", dpi = 110)

# CURVE FITTING 
# CONSTRAIN THE OPTIMIZATION TO THE REGION of e.g. 0 <= a <= 5, 0 <= b <= 1 and 0 <= c <= 0.5:
"""Two small separate data frames has to be created so the curbe fitting can be performed
   on each of them separately!"""
a = pd.read_csv("aggregated.csv")
a = a.sort_values("RC (ugTOC/cell)")
z = a["RC (ugTOC/cell)"]
cc2 = a["TCCM2 (#/mL)"]
cc3 = a["TCCM3 (#/mL)"]

data2 = {"RC": z, "TCC2": cc2}
data3 = {"RC": z, "TCC3": cc3}
df2 = pd.DataFrame(data2, index=range(0, len(z)))
df2 = df2[df2.TCC2 != 0]
df3 = pd.DataFrame(data3, index=range(0, len(z)))
df3 = df3[df3.TCC3 != 0]

x2 = df2["RC"]
tc2 = df2["TCC2"]
x3 = df3["RC"]
tc3 = df3["TCC3"]

def func(x, a, b):
    return a/x+b
   
popt, pcov = curve_fit(func, x2, tc2)
par2 = popt

popt2, pcov2 = curve_fit(func, x3, tc3)
par3 = popt2

# PLOT BOTH MODELS AND OBSERVED DATA
fig, ax = plt.subplots()
plt.plot(x, func(x, *popt), 'g:',
              label='fit M2: a=%5.1f, b=%5.1f' % tuple(popt))
plt.plot(x, func(x, *popt2), 'r:',
              label='fit M3: a=%5.1f, b=%5.1f' % tuple(popt2))
plt.scatter(x, tcc2, label="$\Delta$TCC M2")
plt.scatter(x, tcc3, label="$\Delta$TCC M3")
plt.xlabel("R/C [$\mu$gTOC/cell]", fontsize=12)
plt.ylabel("$\Delta$TCC [#/mL]", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.xscale("log")
ax.set_ylim([-2.4*10**(7), 3*10**6])
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
plt.legend()
plt.savefig('figures/agg_fit.png', bbox_inches = "tight", dpi = 110)