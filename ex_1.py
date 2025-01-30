#!/usr/bin/env python
# coding: utf-8

import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import interactive, Select, interact

sns.set()

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))

sex_options = tips['sex'].unique()
time_options = tips.time.unique().tolist()
smoker_options = tips.smoker.unique().tolist()

def update_chart(smoker, time):
    sns.lineplot(x='total_bill', y='tip', hue='day',
                 data=tips[(tips['smoker'] == smoker) & (tips['time'] == time)])
    plt.show()

interact(update_chart,
         smoker=Select(options=smoker_options),
         time=Select(options=time_options));
