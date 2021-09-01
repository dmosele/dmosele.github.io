#!/usr/bin/env python
# coding: utf-8

# # Lists and Iterating

# Let's take a deeper dive in our look at lists as well as the idea of a for loop. A for loop allows us to do a repetitive process a given number of times and is sometimes the easiest way to accomplish this. Later in the course we will learn that we can sometimes avoid using loops and if we are trying to be efficient, we should keep this in mind. At the end of this lesson, we will learn a special feature of Python called "list comprehension" which allows us to define a list by a for loop.

# First, we will look at the basics of a for loop. In a for loop, we execute code a number of times and the code can depend on which iteration it is. For example

# In[1]:


#To write a for loop, you specify an iterating variable and tell it what values to take.
#Here we tell the variable i to take the values 0, 1, and 2
#After writing the for statement, you include a colon
for i in range(10):
    #whatever code is executed by the for loop is offset by an indent or 4 spaces
    print(i)


# $\underline{\hspace{6in}}$

# To do something a little more interesting, we write out the Fibonacci sequence using a for loop.

# In[2]:


#Create the Fibonacci sequence using a for loop
a=1
b=1
c = a + b
print(a,b,c,sep='\n')


for i in range(20):
    a = b
    b = c
    c = a+b
    print(c)


# In[3]:


#Create the Fibonacci sequence in a list
fib = [1,1]

for i in range(20):
    fib.append(fib[i]+fib[i+1])
    
print(fib)


# $\underline{\hspace{6in}}$

# We can also use a for loop to create a list. Next, we will create a list of numbers from 0 to 99. Certainly we don't want to do this by writing out all of these numbers!

# In[4]:


#Start with an empty list and use a loop to populate the list with the numbers from 0 to 99
listonumbers = []

for j in range(100):
    listonumbers.append(j)
    
print(listonumbers)


# $\underline{\hspace{6in}}$

# While we can iterate a for loop using a sequence of numbers, we can also iterate through a list. Let's see an example of this.

# In[5]:


#Print out the lyrics of the Alma Mater, each lyric on a new line
AlmaMater = ['On','the','banks','of','the','wide','St.','Johns']

for w in AlmaMater:
    print(w)


# $\underline{\hspace{6in}}$

# Finally, let's try this same task using a cool Python feature called list comprehension.

# In[6]:


#Create a list that generates the first 100 square numbers
Y = [i**2 for i in range(100)]

print(Y)


# Typically the way we use this involves manipulating our iterator in some way. Perhaps we want to do a repetitive calculation.

# In[ ]:




