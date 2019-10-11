#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Compreensão em listas


# In[9]:


x = []

for i in range(0,10):
    x += [i]


# In[10]:


x


# In[5]:


x2 = [i for i in range(0,10)]


# In[11]:


x2


# In[12]:


x3 = [i*2 + 10 for i in range(0,15)]


# In[13]:


x3


# In[14]:


#Criação de listas pares


# In[21]:


a = []

for i in range(0,21):
    if i % 2 == 0:
        a += [i]


# In[22]:


a


# In[25]:


x = [i for i in range(0,21) if i % 2 == 0]


# In[26]:


x


# In[34]:


lista = []
lista = [letter for letter in 'word']


# In[35]:


lista


# In[36]:


#Conversão de temperaturas de Celcius para Fahrenheit


# In[37]:


celsius = [0,10,15,20,30,50,100]


# In[38]:


fah = [(temp * (9/5) + 32) for temp in celsius]


# In[39]:


fah


# In[ ]:




