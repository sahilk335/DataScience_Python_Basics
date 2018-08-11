# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:31:57 2018

@author: sahil

Title : Plot lines
    
"""

import matplotlib.pyplot as plt

x=[1,2,3]
y=[4,5,6]

plt.plot(x,y,label="line",color='r')
#legend displays the info box
plt.legend()
plt.show()
