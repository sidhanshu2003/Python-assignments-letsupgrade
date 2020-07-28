#!/usr/bin/env python
# coding: utf-8

# In[3]:


str = 'What we think we become; we are python programmers'
index = 0
while index < len(str):
    index = str.find('we', index)
    
    # If index value is -1. Come out of loop
    if index == -1:
        break
    
    # If index value is other than -1 that means we is found. Print index value of we
    print('We found at', index)
   
    # Increment by 2 in next iteration as we consists of 2 index values
    index = index + 2


# In[4]:


str = "Hello World"
str.islower()


# In[6]:


str = "hello world"
str.islower()


# In[7]:


str = "hello World"
str.islower()


# In[9]:


str = "Hello World"
str.isupper()


# In[10]:


str = "HELLO World"
str.isupper() 


# In[11]:


str = "HELLO WORLD"
str.isupper() 




