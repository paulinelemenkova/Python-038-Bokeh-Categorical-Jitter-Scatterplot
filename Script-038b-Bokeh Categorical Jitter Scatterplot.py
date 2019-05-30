#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
from matplotlib import pyplot as plt
from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.transform import jitter
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
import os

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")
df = df.melt(id_vars=['observ'], 
              value_vars=["profile1", "profile2", "profile3", "profile4","profile5",
            "profile6", "profile7","profile8", "profile9", "profile10",
            "profile11", "profile12", "profile13", "profile14", "profile15",
            "profile16", "profile17", "profile18", "profile19", "profile20",
            "profile21", "profile22", "profile23", "profile24", "profile25"],
             var_name='profile', value_name='Depth')

profile = ["profile1", "profile2", "profile3", "profile4","profile5",
            "profile6", "profile7","profile8", "profile9", "profile10",
            "profile11", "profile12", "profile13", "profile14", "profile15",
            "profile16", "profile17", "profile18", "profile19", "profile20",
            "profile21", "profile22", "profile23", "profile24", "profile25"]

source = ColumnDataSource(df)

#profile_cmap = factor_cmap('profile', palette=Spectral6,
 #                          factors=sorted(df.profile.unique()), start=1, end=25)

p = figure(plot_width=800, plot_height=300, y_range=profile, 
           title="Categorical jitter plot of range of the bathymetric values,\n Mariana Trench, 25 profiles")

#p.circle(x='Depth', y=jitter('profile', width=1.2, range=p.y_range), fill_color=profile_cmap, 
#         source=source, alpha=0.3)
p.circle(x='Depth', y=jitter('profile', width=1.2, range=p.y_range), source=source, alpha=0.3)

show(p)

