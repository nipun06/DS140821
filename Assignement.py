#!/usr/bin/env python
# coding: utf-8

# In[3]:


class power:
    def __init__(self,a,n):
        self.a=a
        self.n=n
        self.result=0
        
    def power(self):
        self.result=pow(self.a,self.n)
        print(self.result)


# In[4]:


find = power(10,2)


# In[6]:


find.n_power()


# In[ ]:




