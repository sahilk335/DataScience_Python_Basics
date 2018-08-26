# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:39:47 2018

@author: sahil

Title : 
"""
import quandl
import pandas as pd

# df = quandl.get("FMAC/HPI_AK", authtoken="j_FPd8gs3sP2JP9P3fD_", start_date="2014-01-31")
# print(df.head())

US_State = pd.read_html('https://www.factmonster.com/us/postal-information/state-abbreviations-and-state-postal-codes')

# print(US_State)

# This prints the first data frames
# print(US_State[0])

# Get the columns
# print(US_State[0][2])

for abbv in US_State[0][2][1:]:
    print("Sahil- abbv - " + abbv + "\n")