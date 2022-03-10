#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel('copia.xlsx')


# In[3]:


df.head()


# In[10]:


def rentabilidade(data_i, data_f):
    dft=df.loc[df["Data"].between(data_i, data_f)]
    
    x = dft['Fundo Total Return'].iloc[-1]
    
    y = dft['Fundo Total Return'].iloc[1]
    
    z = round((x/y)-1, 2)
    
    return z


# In[11]:


rentabilidade('2019-01-01', '2020-01-01') #exemplo de uso


# In[ ]:





# In[ ]:




