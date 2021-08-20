#!/usr/bin/env python
# coding: utf-8

# # More Mathematical Operations in Python
# 
# Here we are going to lean on the math module in Python to unlock some more advanced mathematical operations. To import a module, you just use the code "import nameofmodule". (Though we will later learn some different ways to import modules).

# In[1]:


# try out import math
import math


# Let's now see what we can do with the math module. Perhaps something we can compute in multiple ways like square root. Compute $\sqrt{2}$ using an exponent as well as math.sqrt(2).

# In[2]:


# Compute the square root of 2 using the code math.sqrt(2)
math.sqrt(2)


# In[3]:


# Which exponent is equivalent to the square root?
2**(1/2)


# What about other mathematical functions such as $\sin(x)$, $e^x$, and $\log(x)$? If you are pausing here because you either don't remember these functions or are wondering "which log", that's totally okay. The logarithm function is a good example of one that can take several arguments (inputs). Python sometimes makes assumptions about your input if you leave out optional inputs. 

# In[4]:


#Compute math.sin(3.14159)
math.sin(3.14159)


# In[5]:


#Compute math.exp(2)
math.exp(2)


# In[6]:


#Compute math.log(100,10) and math.log(100)
print(math.log(100,10),math.log(100),sep='\n')


# My computation of $\sin(\pi)$ earlier was kind of weak because I used an approximation. A better approximation for $\pi$ is contained in the math module as math.pi. Can we do that computation again?

# In[7]:


#Compute sin(pi) using the pi value from the math module

math.sin(math.pi)


# $\underline{\hspace{6in}}$

# One more topic to bring up is rounding. There are several ways to go about rounding a number. We could always round up, always round down, or just round to the nearest whole number. The first is frequently referred to as the "ceiling" function, the second is the "floor" function, and the last is usually what we just call rounding.
# 
# The ceiling function is math.ceil, the floor is math.floor, and rounding can be achieved with the round() function. Note that the round() function can take more than one input. What might the second input specify when rounding?

# In[8]:


#Compute the ceiling, floor, and rounded value of pi.

print(math.floor(math.pi),math.ceil(math.pi),round(math.pi,5),sep='\n')


# Finally, let's have a look at one of the pitfalls of computation on a computer. That is, it isn't great with exact values. For example, I know the algebraic identity that 
# $$ e^{\log(x)} = x .$$
# However, if we compute $e^{\log(20)}$ what do we get?

# In[9]:


#Compute e^(log(20))
math.exp(math.log(20))


# In[10]:


math.exp(1)**math.log(20)


# In[ ]:




