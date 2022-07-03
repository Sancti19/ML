#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os


# In[2]:


pwd


# In[3]:


os.chdir('C:\\Users\\Blaise Hilary\\Downloads')


# In[4]:


data = pd.read_csv('AB_NYC_2019.csv')


# In[5]:


data.head()


# In[6]:


data.shape


# In[7]:


data.price.max()


# In[8]:


data.price.min()


# In[9]:


data.price.mean()


# In[10]:


data[data.price == 10000]


# ## Detecting outliers

# In[11]:


max_threshold = data['price'].quantile(0.95)
max_threshold


# In[12]:


data[data.price > max_threshold]


# In[18]:


min_threshold = data['price'].quantile(0.05)
min_threshold


# In[19]:


data[data.price < min_threshold]


# ## Remove outliers 

# In[29]:


data[(data['price'] > min_threshold) | (data['price'] < max_threshold)]


# 

# In[ ]:




