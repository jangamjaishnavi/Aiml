#!/usr/bin/env python
# coding: utf-8

# In[36]:


def mean_value(L):
    if len(L)==0:
        return 0
    else:
        avg = sum(L)/len(L)
        return avg


# In[37]:


L=[2,3,4,5]
mean_value(L)


# In[53]:


def mode_value(L):
    s = set(L)
    d={}
    for x in s:
        d[x]=L.count(x)
    return(max(d.values()))


# In[49]:


L=["M","F","M"]
mode_value(L)


# In[55]:


def mode_value(L):
    s = set(L)
    d={}
    for x in s:
        d[x]=L.count(x)
    m=max(d.values())
    for k in d.keys():
        if d[k]==m:
            return k
    return(max(d.values()))


# In[57]:


L=[1,2,3,1,4,1,5]
mode_value(L)


# In[ ]:




