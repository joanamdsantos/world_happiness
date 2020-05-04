import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_countrybarplot(df, var, top_num):
    '''
    INPUT:
        df - pandas dataframe with the data
        var- variable to plot, not categorical
        top_num - number of top countries to plot
    OUTPUT:
        plot with the top number of countries with the var scores
    '''
    
   # Initialize the matplotlib figure
    f, ax = plt.subplots(figsize=(6, 15))
    
   # Choose only the top 50 countries with higher score
    y=df.sort_values(var, ascending=False)
    y_top = y['Country or region'][:top_num]

    # Plot the GDP per capita per country
    sns.set_color_codes("pastel")
    g=sns.barplot(x=var, y=y_top, data=df,
               label=var, color="y")

    # Add a legend and informative axis label
    ax.legend(ncol=3, loc="lower right", frameon=True)
    ax.set(xlim=(0, 10), ylabel="",
           xlabel=var)
    sns.despine(left=True, bottom=True)
    
    return g