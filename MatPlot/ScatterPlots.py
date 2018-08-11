# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:58:04 2018

@author: sahil

Title : ScatterPlots

"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='g', s=25, marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plots')
plt.legend()
plt.show()