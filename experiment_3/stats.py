# -*- coding: utf-8 -*-

"""
Created on some point in time

@author: Nash
"""

def mean(vector):
    mx = sum(vector)/len(vector)
    return mx

def var(vector):
    variance = 0
    dx = 0
    for i in vector:
        dx += (i - mean(vector))**2
        variance = dx/(len(vector)-1)
    return variance
    

def std(vector):
    sx = (var(vector))**0.5
    return sx
    

def ste(vector):
    smx = (var(vector)/len(vector))**0.5
    return smx