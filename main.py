# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:03:07 2022

@author: sm18aeh
"""

import pandas as pd
import matplotlib.pyplot as plt

#reading data sheet
df = pd.read_excel("regionalgrossdomesticproductgdplocalauthorities.xlsx",
                   sheet_name="Table 6",header=1)

print(df.head(5)) #checking the sheet has been read correctly

london = df[df["ITL1 Region"] == "London"] #data from london boroughs only
print(london.head(5))#checking the previous line has exectued as intended

names = london["LA name"] #names of london boroughs

barnet = london.loc[names == "Barnet"].iloc[:,3:] #getting the value columns from a specific row
print(barnet.T) #printing the transposed dataframe

#line graph of Barnet's population
plt.figure()
plt.plot(barnet.T,label="Barnet")
plt.xlim("1998","2020")
plt.xticks([str(i) for i in range(1998,2021,2)]) #reducing clutter on axis markings
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Barnet resident population")
plt.show()

#new figure containing all london boroughs
plt.figure()
#plotting every london borough, iterating by name
for i in names:
    plt.plot(london.loc[names == i].iloc[:,3:].T,label=i)
    
plt.xlabel("Year")
plt.ylabel("Population")
plt.xticks([str(i) for i in range(1998,2021,2)])#reducing clutter on axis markings
plt.legend()
plt.show()
