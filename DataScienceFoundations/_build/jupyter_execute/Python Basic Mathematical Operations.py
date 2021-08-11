#!/usr/bin/env python
# coding: utf-8

# # Basic Mathematical Operations in Python

# For the most part, mathematical operations work just like you would like in Python. For example, let's add 3 and 5 by typing "3+5". To execute code in a Jupyter Notebook cell, you press Shift+Enter.

# In[1]:


3+5


# Python then reports the answer correctly as 8.
# 
# The same is true for multiplication and division.

# In[2]:


3*5


# In[3]:


5/3


# If we want to exponentiate however, the typical caret symbol doesn't work. In fact, it has to do with the "exclusive or" logical operation.

# In[4]:


3^5


# Using two asterisks though yields the desired result.

# In[5]:


3**5


# Most of the time, we will actually be using variables to represent numbers (and strings, lists, matrices, etc). Let's have a look at some computations when using variables.

# In[6]:


x = 5
y = 3
print(x+y,x*y,y**x,x/y,sep='\n')


# If we want to play with a couple of more nuanced operations, using two forward slashes represents division and round to the nearest integer. The percent symbol is the modulus of a number, or the remainder when you divide one number by another.

# In[7]:


x//y


# In[8]:


x%y


# Note that in my notebook, Python is remembering that I assigned x the value 5 and y the value 3.

# In[ ]:




