#!/usr/bin/env python
# coding: utf-8

# # Lists and Iterating #2

# Let's create a loop that adds up the first few odd numbers such as 
# $$1+3+5+7+9 = 25$$
# This is easy to do when you add up a limited number of odd numbers, but if we were doing this 20, 50, or 100 times, a loop would make our lives much easier.

# In[1]:


#Write a loop that adds up the first 20, 50, or 100 odd numbers. 
#Is there a pattern here?

sum_of_odds=0

for i in range(100):
    sum_of_odds = sum_of_odds + (2*i+1)

print(sum_of_odds)


# Next, create a loop that adds up terms of the form $\frac 1{n^2}$. That is, if we for example add up the first 4
# $$\frac 1{1^2} + \frac 1{2^2} + \frac{1}{3^2} + \frac{1}{4^2}.$$
# Write a loop to add up the first 10000 of these.

# In[2]:


# Add up the sequence of fractions above using a loop.
# You may want to start at 1

sum_of_fracs = 0

for j in range(10000):
    sum_of_fracs = sum_of_fracs + (1/((j+1)**2))

print(sum_of_fracs)


# Unrelated but interesting, what happens when you take the answer above, multiply it by 6 and then take the square root?

# In[3]:


(6*sum_of_fracs)**(1/2)


# $\underline{\hspace{6in}}$

# Here are a few (one of them silly) examples of loops.

# In[4]:


bingo = "There was a farmer had a dog and Bingo was his name-oh"
name = 'BINGO'
ending = "and Bingo was his name-oh"

for i in range(5):
    print(bingo)
    print(name[i:],name[i:],name[i:],sep=', ')
    print(ending)


# In[5]:


#approximating the number e
import math

sum = 0

for i in range(30):
    sum = sum + (1/math.factorial(i))
    
print(sum)


# In[6]:


#tribonacci numbers

trib = [0,1,1]

for k in range(30):
    trib.append(trib[k]+trib[k+1]+trib[k+2])
    
print(*trib,sep='\n')


# In[ ]:




