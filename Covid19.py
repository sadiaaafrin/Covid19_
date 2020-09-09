#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[27]:


data = pd.read_csv("C:/Users/Sadia/Downloads/COVID-19-geographic-disbtribution-worldwide.csv")


# In[28]:


data.head()


# In[29]:


data.describe()


# # Relating the variable with scatterplots

# In[34]:


sns.relplot(x= 'continentExp', y = 'cases', data = data)


# In[50]:


sns.catplot(x = 'month', y = 'deaths', data = data)


# In[60]:


sns.jointplot(x = 'cases', y = 'deaths', data = data, alpha = 0.5, edgecolor = 'black')


# In[63]:


sns.heatmap(data.corr(),annot = True)


# In[ ]:




