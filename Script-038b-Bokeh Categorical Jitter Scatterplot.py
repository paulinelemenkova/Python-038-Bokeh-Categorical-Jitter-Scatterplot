#!/usr/bin/env python
# coding: utf-8
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

# defining loop sequence
profiles_nrs = list(map(lambda x: x, range(25)))
profiles_list = []
for i in profiles_nrs:
    profiles_list.append('profile{}'.format(i + 1))

df = df.melt(id_vars = ['observ'],
             value_vars = profiles_list,
             var_name='profile', value_name='Depth')

profile = profiles_list

source = ColumnDataSource(df)

p = figure(plot_width=800, plot_height=300, y_range=profile,
           title="Categorical jitter plot of range of the bathymetric values,\n Mariana Trench, 25 profiles")

p.circle(x='Depth', y=jitter('profile', width=1.2, range=p.y_range), source=source, alpha=0.3)

show(p)
