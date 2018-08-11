# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:45:30 2018

@author: sahil

Title : Bar Graphs

"""

import matplotlib.pyplot as plt

x1=[1,2,3,4,5]
y1=[9,6,4,3,2]

plt.bar(x1,y1, label="Bars1")

x2=[2,4,6,8,10]
y2=[8,6,2,5,6]
plt.bar(x2,y2, label="bars2", color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Bar Graphs')

plt.show()

