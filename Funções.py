#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Funções


# In[8]:


def primeira_funcao():
    print('Olá mundo')


# In[9]:


primeira_funcao()


# In[12]:


def somar(num1,num2):
    print(num1+num2)


# In[15]:


somar(3,4)


# In[16]:


def mais(num1,num2):
    return num1+num2


# In[31]:


x = mais(5,4)


# In[32]:


x


# In[35]:


def primo(num):
    """
    Método para checar se é primo
    """
    for n in range(2,num):
        if num % n == 0:
            print('Não é primo')
            break
    else:
        print('Primo')


# In[36]:


primo(2)


# In[37]:


primo(4)


# In[38]:


primo(17)


# In[39]:


def primo(num):
    """
    Método para checar se é primo
    """
    def divisivel(a,b):
        return a % b
    
    for n in range(2,num):
        if divisivel(num,n) == 0:
            print('Não é primo')
            break
    else:
        print('Primo')


# In[40]:


primo(2)


# In[ ]:




