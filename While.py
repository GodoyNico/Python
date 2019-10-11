#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = 1
y = 1


# In[6]:


while x <= 10 and y <= 20:
    print('O valor de x é {0} e o valor de y é {1}.'.format(x,y))
    x += 1
    y += 2
else:
    print('O valor de x*y é: {0}'.format(x*y))


# In[7]:


#Break


# In[8]:


x = 1
lista = []


# In[9]:


while True:
    lista += [x]
    x += 1
    if x > 10:
        break


# In[10]:


lista


# In[12]:


#Continue


# In[25]:


ate = 50
x = 0


# In[26]:


while x < ate:
    x += 1
    if x % 2 == 1:
        continue
    if x % 2 == 0:
        print(x,'é par')


# In[ ]:




