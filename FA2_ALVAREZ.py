#!/usr/bin/env python
# coding: utf-8

# In[1]:


def multiply(numbers):
    product = 1
    for num in numbers:
        product *= num
    
    return product


# In[3]:


numbers =[5, 6, -1, 2, 4, -2, -10, 7]

multiply(numbers)


# In[20]:


def border():
    print('+ - - - - + - - - - + - - - - + - - - - +')
   
def bars():
    print('|         |         |         |         |')


# In[21]:


border()
bars()
bars()
bars()
bars()
border()
bars()
bars()
bars()
bars()
border()
bars()
bars()
bars()
bars()
border()
bars()
bars()
bars()
bars()
border()


# In[ ]:




