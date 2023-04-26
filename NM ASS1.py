#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams


# In[2]:


df=pd.read_csv('C:/Users/karuna/Downloads/archive/House Price India.csv')
df


# In[ ]:


##descriptive analysis


# In[4]:


df.shape


# In[8]:


df.info()


# In[7]:


df.size


# In[9]:


df.median()


# In[11]:


df.describe()


# In[13]:


df.corr()


# In[15]:


df.head()


# In[17]:


df.tail()


# In[19]:


df.mean()


# In[21]:


df.sum()


# In[23]:


df.sum(1)


# In[25]:


df.std()


# In[27]:


df.columns


# In[29]:


df.count()


# In[32]:


df.mode()


# In[35]:


df.min()


# In[18]:


df.cumsum()


# In[39]:


df.abs()


# In[37]:


df.max()


# In[15]:


import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams


# In[16]:


df=pd.read_csv('C:/Users/karuna/Downloads/archive/House Price India.csv')


# In[17]:


df.cumprod()


# In[ ]:


#handling missing elements


# In[19]:


df.isnull()


# In[43]:


df.isnull().sum()


# In[4]:


#piechart


# In[3]:


plt.pie(df['number of bathrooms'])
plt.show()


# In[ ]:


#univariate analysis


# In[5]:


x=sns.catplot(x='number of bedrooms',data=df)
plt.show()


# In[ ]:


##bivariate analysis


# In[6]:


x=sns.catplot(x='number of bathrooms',y='lot area',data=df)
plt.show()


# In[7]:


plt.hist(df['living area'])
plt.show()


# In[8]:


sns.lineplot(x=df.index,y=df['living area'])
plt.show


# In[9]:


plt.hist(df['living area'])
plt.show()


# In[10]:


sns.scatterplot(x=df.index,y=df['number of bedrooms'])
plt.show()


# In[5]:


##multivariate


# In[20]:


df.hist()  


# In[ ]:




