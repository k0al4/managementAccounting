#!/usr/bin/env python
# coding: utf-8

# In[73]:


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


# In[3]:


tips.sample(5)


# In[53]:


import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['volume','contribution','totContribution','fCosts','profit'])
for c in [x for x in np.arange(1,50,1)]:
    for fc in [500000,600000,700000,800000]:
        for v in [w for w in range(0,1000000,50000)]:
            df.loc[len(df)] = [v,c,v*c,fc,v*c-fc]

df = df.assign(bep=df.fCosts/df.contribution)


# In[14]:


import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact
import numpy as np

def calc_bep(c,fc):
    ax = sns.lineplot(x=[a for a in np.arange(1,c)], y=[fc/d for d in np.arange(1,c)])
    ax.set(xlabel='Contribution margin', ylabel='Break-even point', title='Break-even analysis')
    plt.show()

interact(calc_bep,
         c = widgets.IntSlider(value=3,min=3,max=100,step=1),
         fc = widgets.IntSlider(value=100000,min=100000,max=5000000,step=50000));


# In[129]:


np.where(np.array(revenue) == np.array(cost))[0][0]


# In[204]:


p,v,fc,c = 400,2099,250001,200
revenue = [v*p for v in np.arange(0,v)]
cost = [fc+(p-c)*v for v in np.arange(0,v)]
volume = [n for n in np.arange(0,v)]
print(len(revenue),len(cost),len(volume))
try:
    intersection = np.where(np.array(revenue) == np.array(cost))[0][0]
except:
    intersection = None


# In[206]:


h = plt.plot(volume,[fc for n in np.arange(0,v)],label='Fixed cost',linestyle="-.")


# In[209]:


h[0].get_xdata()


# In[191]:


[a for a,b in zip(revenue,cost) if a == b]


# In[187]:


np.where(np.array(revenue) == np.array(cost))


# In[25]:


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


# In[30]:


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

p,c,fc,v = 400,100,500000,9999

fig,ax = plt.subplots()

revenue = [v*p for v in np.arange(0,v)]
cost = [fc+(p-c)*v if c < p else fc+0*v for v in np.arange(0,v)]
volume = [n for n in np.arange(0,v)]
try:
    bep = volume.index(round(getBEP(fc,c,p)))
except ValueError:
    bep = round(getBEP(fc,c,p))

revLine = ax.plot(volume, revenue,label='Total revenue',linestyle='-')
costLine = ax.plot(volume, cost,label='Total cost',linestyle='--')
volumeLine = ax.plot(volume,[fc for n in np.arange(0,v)],label='Fixed cost',linestyle="-.")
if getBEP(fc,c,p) <= v and c < p:
    bepLine = ax.scatter(bep,revenue[bep])
else:
    pass
ax.text(1, 1, f'BEP: {bep}', fontsize = 16)
ax.legend()
plt.xlabel('Volume sold or capacity')
plt.ylabel('Revenue or costs')
plt.title('Break-even analysis')
plt.show()
    
def updateChart(p,c,fc,v):
    volume = [n for n in np.arange(0,v)]
    for l in [revLine,costLine,volumeLine]:
        l[0].set_xdata(volume)
    revLine[0].set_ydata([v*p for v in np.arange(0,v)])
    costLine[0].set_ydata([fc+(p-c)*v if c < p else fc+0*v for v in np.arange(0,v)])
    volumeLine[0].set_ydata([n for n in np.arange(0,v)])
    try:
        bep = volume.index(round(getBEP(fc,c,p)))
    except ValueError:
        bep = round(getBEP(fc,c,p))
    if getBEP(fc,c,p) <= v and c < p:
        pass
    else:
        pass

interact(
    updateChart,
    p = widgets.FloatSlider(value=400,min=25,max=999,step=1,description='Price'),
    c = widgets.IntSlider(value=100,min=1,max=600,step=1,description='Contribution'),
    fc = widgets.IntSlider(value=500000,min=1,max=2000000,step=2000,description='Fixed costs'),
    v = widgets.IntSlider(value=9999,min=3,max=9999,step=1,description='Capacity'));


# In[23]:


bepLine.get_paths()[0]


# In[2]:


p = widgets.FloatSlider(value=400,min=25,max=999,step=1)


# In[6]:


p.value


# In[117]:


np.where(np.array(revenue) == np.array(cost))[0][0]


# In[64]:


x[1:],x[:-1]


# In[53]:


import numpy as np

# let us generate fake test data
x = np.arange(10)
y1 = np.random.rand(10) * 20
y2 = np.random.rand(10) * 20

z = y1-y2
dx = x[1:] - x[:-1]
cross_test = np.sign(z[:-1] * z[1:])

x_intersect = x[:-1] - dx / (z[1:] - z[:-1]) * z[:-1]
dx_intersect = - dx / (z[1:] - z[:-1]) * z[:-1]

areas_neg = 0.5 * dx_intersect * abs(z[:-1]) + 0.5 * (dx - dx_intersect) * abs(z[1:])
areas_pos = abs(z[:-1] + z[1:]) * 0.5 * dx

areas = np.where(cross_test < 0, areas_neg, areas_pos)
total_area = np.sum(areas)

negatives = np.where(cross_test < 0)
positives = np.where(cross_test >= 0)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, z)
plt.vlines(x_intersect[negatives], -20, 20)

