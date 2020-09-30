#!/usr/bin/env python
# coding: utf-8

# ### Write a function that takes in a Proth Number and uses Proth's theorem to determine if said number is prime? 

# In[2]:


def isprime(n):
    a = 1
    while a>=1:
        if (a**((n-1)/2))%n+1 == n:
            break 
        a = a+1
    return True
    


# In[3]:


x = int (input("Input Proth Number "))

if isprime(x):
    print (x, 'is prime')


# In[ ]:




