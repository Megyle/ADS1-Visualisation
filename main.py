# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:03:07 2022

@author: sm18aeh
"""

import pandas as pd
import matplotlib.pyplot as plt


def line_graph(borough_df):
    """
    Takes a dataframe of a london borough and creates
    a single line plot
    """
    #extracting the name of the borough
    name = borough_df["LA name"].iloc[0]
    plt.figure()
    #plotting the values from the passed row
    plt.plot(borough_df.iloc[:,3:].T)
    plt.xlim("1998","2020")
    #reducing clutter on axis markings
    plt.xticks([str(i) for i in range(1998,2021,2)])
    plt.grid()
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(f"{name} resident population")
    plt.savefig('figure1.png')
    plt.show()
    
def london_line(london_df,sub_reg):
    """
    Takes the dataframe containing london boroughs,
    and a list containing each borough categorised by sub-region.
    Then plots the population of each borough between 1988 and 2020.
    This is divided into 5 subplots, one for each sub-region.
    """    
    sub_reg_names = ["North","South","East","West","Central"]
    #new figure containing all london boroughs 
    plt.figure(figsize=(25,20))
    #iterating for every sub-region
    for i in range(0,5):
        plt.subplot(3, 2, i+1)
        #for every borough in the current iteration's sub-region 
        for j in sub_reg[i]:
            plt.plot(london_df.loc[names == j].iloc[:,3:].T,label=j)
        
        plt.title(sub_reg_names[i]+" London")
        #reducing clutter on axis markings
        plt.xticks([str(i) for i in range(1998,2021,2)])
        plt.xlim("1998","2020")
        plt.grid()
        plt.legend()
        plt.xlabel("Year")
        plt.ylabel("Population")
    
    plt.savefig('figure2.png')
    plt.show()

def pie_chart(london_df,sub_reg):
    """
    Takes the dataframe containing london boroughs,
    and a list containing each borough categorised by sub-region.
    Then calculates the total population (2020) of each sub-region
    and plots the result on a pie chart.
    """
    #this will contain the sum of all sub-regions
    #and will be used to plot the pie chart
    reg_sum = [0,0,0,0,0]
    sub_reg_names = ["North","South","East","West","Central"]
    #iterating for every sub-region
    for i in range(0,5):
        #for every borough in the current iteration's sub-region
        for j in sub_reg[i]:
            reg_sum[i] += london_df.loc[names == j].iloc[0,-1]
    #creating the pie chart
    plt.figure()
    plt.pie(reg_sum,labels=sub_reg_names,autopct="%1.1f%%")
    plt.title("2020 Greater London Population by Sub-region")
    plt.savefig('figure3.png')
    plt.show()

def bar_chart(left_borough, right_borough):
    """
    Takes two dataframes of london boroughs and creates a bar plot 
    allowing their populations over the years to be compared.
    """
    #getting the name of each borough
    left_name = left_borough["LA name"].iloc[0]
    right_name = right_borough["LA name"].iloc[0]

    plt.figure()
    #setting a custom range of years for better readability
    years = [2000, 2004, 2008, 2012, 2016, 2020]
    #setting offset for left bar
    left_years = [i-1 for i in years]
    left_borough = left_borough[[str(i) for i in years]].T.iloc[:,0]
    plt.bar(left_years, left_borough, width=1.5,label=left_name)
    
    #setting offset for right bar
    right_years = [i+1 for i in years]
    right_borough = right_borough[[str(i) for i in years]].T.iloc[:,0]
    plt.bar(right_years, right_borough, width=1.5,label=right_name)
    
    plt.legend()
    plt.title(f"{left_name} and {right_name} population between 2000 and 2020")
    plt.xticks(years)
    plt.xlim(1998,2022)
    plt.savefig('figure4.png')
    plt.show()
    
    
if __name__ == "__main__":
    #reading data sheet
    df = pd.read_excel("regionalgrossdomesticproductgdplocalauthorities.xlsx",
                       sheet_name="Table 6",header=1)
    #checking the sheet has been read correctly
    print(df.head(5))
    #data from london boroughs only
    london_df = df[df["ITL1 Region"] == "London"] 
    #checking the previous line has exectued as intended
    print(london_df.head(5))
    #names of london boroughs
    names = london_df["LA name"]
    #selecting a specific row
    barnet_df = london_df.loc[names == "Barnet"]
    #creating a line graph for Barnet
    line_graph(barnet_df)
    
    #London boroughs grouped by sub-region
    c_lon = ["City of London","Camden","Islington","Kensington and Chelsea",
             "Lambeth","Southwark","Westminster"]
    n_lon = ["Barnet","Enfield","Haringey"]
    s_lon = ["Bromley","Croydon","Kingston upon Thames",
             "Merton","Sutton","Wandsworth"]
    e_lon = ["Barking and Dagenham","Bexley","Greenwich",
             "Hackney","Havering","Lewisham","Newham",
             "Redbridge","Tower Hamlets","Waltham Forest"]
    w_lon = ["Brent","Ealing","Hammersmith and Fulham",
             "Harrow","Hillingdon","Hounslow","Richmond upon Thames"]
    #grouping all sub-regions into a list for iteration in procedures
    sub_reg = [n_lon,s_lon,e_lon,w_lon,c_lon]
    
    #creating a line graph for all london boroughs
    london_line(london_df,sub_reg)
    #creating a pie chart for all london boroughs
    pie_chart(london_df,sub_reg)
    
    #selecting a specific row from london_df
    camden_df = london_df.loc[names == "Camden"]
    #creating a bar graph of two london boroughs
    bar_chart(barnet_df,camden_df)