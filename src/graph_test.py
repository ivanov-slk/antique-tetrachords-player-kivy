# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:26:44 2019

@author: Slav
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
 
# y-axis in bold
rc('font', weight='bold')
 
# Values of each group
bars1 = [0, 1, 8, 22]
bars2 = [0, 16, 4, 10]
bars3 = [0, 23, 25, 17]
 
# Heights of bars1 + bars2 (TO DO better)
bars = [0, 17, 12, 32]
 
# The position of the bars on the x-axis
r = [0,1,2,3]
 
# Names of group and bar width
names = ['A','B','C','D']
barWidth = 1
 
# Create brown bars
plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barWidth)
# Create green bars (middle), on top of the firs ones
plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)
# Create green bars (top)
plt.bar(r, bars3, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)
 
# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("group")
 
# Show graphic
plt.show()


import matplotlib.pyplot as plt
import numpy as np

countries = {'NG': [1405, 7392], 'IN': [5862, 9426], 
             'GB': [11689, 11339], 'ID': [7969, 2987]}

c = []
v = []             
for key, val in countries.items():
    c.append(key)
    v.append(val)
v = np.array(v)

plt.bar(range(len(c)), v[:,0])
plt.bar(range(len(c)), v[:,1], bottom=v[:,0])
plt.xticks(range(len(c)), c)
plt.show()