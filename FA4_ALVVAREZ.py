#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ack(m,n):
    if m == 0:
        return (n + 1, 1)
    elif m > 0 and n == 0:
        a, cnt = ack(m - 1.0, 1.0)
        return a, cnt+1
    elif m > 0 and n > 0:
        a1, cnt1 = ack(m, n - 1.0)
        a2, cnt2 = ack(m - 1.0, a1)
        return a2, 1 + cnt1 + cnt2


# In[19]:


print("ack(2,4) has an output:",ack(2,4)) #for large values of m and n a recursion error occurs


# In[9]:


def is_power(a, b):
   if a < 1:  
       return False     
   elif a == 1:  
       return True
   elif b == 1:        
       return False     
   else:
       return is_power(a / b, b)  


# In[14]:


print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(2048, 2) returns: ", is_power(2048, 2))
print("is_power(14, 5) returns: ", is_power(14, 5))
print("is_power(27, 2) returns: ", is_power(27, 2))


# In[ ]:




