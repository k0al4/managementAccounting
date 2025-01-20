#!/usr/bin/env python
# coding: utf-8

# In[73]:


import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact
import numpy as np

def getTotalProfit(fc,c,v):
    return c*v-fc

def getRevenue(p,v):
    return p*v

def getBEP(fc,c,p):
    if c < p:
        return round(fc/c)
    else:
        return 0

def updateChart(p,c,fc,v):
    fig,ax = plt.subplots()
    revenue = [v*p for v in np.arange(0,v)]
    cost = [fc+(p-c)*v if c < p else fc+0*v for v in np.arange(0,v)]
    volume = [n for n in np.arange(0,v)]
    try:
        bep = volume.index(round(getBEP(fc,c,p)))
    except ValueError:
        bep = getBEP(fc,c,p)
    
    ax.plot(volume, revenue,label='Total revenue',linestyle='-')
    ax.plot(volume, cost,label='Total cost',linestyle='--')
    ax.plot(volume,[fc for n in np.arange(0,v)],label='Fixed cost',linestyle="-.")
    if getBEP(fc,c,p) <= v and c < p:
        ax.scatter(bep,revenue[bep])
    else:
        pass
    ax.text(1, 1, f'BEP: {bep}', fontsize = 16)
    ax.legend()
    plt.xlabel('Volume sold or capacity')
    plt.ylabel('Revenue or costs')
    plt.title('Break-even analysis')
    plt.show()

interact(
    updateChart,
    p = widgets.FloatSlider(value=400,min=25,max=999,step=1,description='Price'),
    c = widgets.IntSlider(value=100,min=1,max=600,step=1,description='Contribution'),
    fc = widgets.IntSlider(value=500000,min=1,max=2000000,step=2000,description='Fixed costs'),
    v = widgets.IntSlider(value=9999,min=3,max=9999,step=1,description='Capacity'));
