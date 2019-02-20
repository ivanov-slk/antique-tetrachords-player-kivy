# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:26:44 2019

@author: Slav
"""
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

### real example
all_items = {'Tempered major': [0, 200, 200, 100],
        'Tempered minor': [0, 200, 100, 200],
        'Archites enharmonic': [0, 62.960903872962575, 48.77038139681492, 386.3137138648348]}

labels = []
data = []
for key, value in all_items.items():
    labels.append(key)
    data.append(val)
    
data = np.array(data)

plt.bar(range(len(labels)), [0, 0, 0])
plt.bar(range(len(labels)), [200, 200, 62.96])
plt.bar(range(len(labels)), [200, 100, 48.770])
plt.bar(range(len(labels)), [100, 200, 368.3137])
#plt.bar(range(len(labels)), data[:, 1], bottom=data[:, 0])
plt.xticks(range(len(labels)), labels)
plt.show()


######################
N = len(labels)
menMeans = tuple(all_items.values())[0]
womenMeans = tuple(all_items.values())[2]
anotherMeans = tuple(all_items.values())[1]
menStd = (2, 3, 4, 1)
womenStd = (3, 5, 2, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans)
p2 = plt.bar(ind, anotherMeans, width,
             bottom=menMeans+womenMeans)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, labels)
#plt.yticks(np.arange(0, 81, 10))
#plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

################ working
a = pd.DataFrame(all_items)
a.T.plot(kind='bar', stacked=True)