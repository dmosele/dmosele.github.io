#!/usr/bin/env python
# coding: utf-8

# # Functions
# When we want to generalize a computation or be able to apply a process to several objects, we can utilize the idea of a function to achieve this. The notion of function is similar to the one in math, except it has a little (just a little) more freedom. In math, a function takes some object as input (a number or numbers usually) and produces an output (also generally a number, but not necessarily). Here, it is essentially the same scenario except our output doesn't even necessarily have to exist!
# 
# To further show the similarities, let's take an example of the squaring function. In a math course, you would typically write the function as
# $$ f(x) = x^2 .$$
# The input is a number for which we use $x$ as a stand-in, and the output is the square of the input.

# In[1]:


#implement the squaring function in code
#square a few numbers

def square(x):
    return x**2


# In[2]:


square(5)


# In[3]:


square(2.718)


# The formatting here should remind you a little of the loops we have implemented before. We always start a function definition with "def" followed by the function name with its input(s) in parentheses and a colon. That is,
# 
# def function_name(variables):
# 
# We then indent the next line and we use "return" to indicate what the output(s) should be.

# $\underline{\hspace{6in}}$
# 
# Let's look at another example. This function will take a string as input and output the string next to itself. That is, if the input is 'dolphin', the output will be 'dolphindolphin'.

# In[4]:


#implement the function that doubles strings

def double_string(word):
    return word+word


# In[5]:


#double the string 'dolphin'

double_string('dolphin')


# In[6]:


#apply the function to another string

double_string('blah')


# In[7]:


#Note that this function doesn't have to be used on a string

double_string(5)


# $\underline{\hspace{6in}}$
# 
# Perhaps a more useful example could be converting temperatures in Fahrenheit to Celsius. Recall that the conversion here is 
# $$C = (F-32)*(5/9)$$

# In[8]:


#implement the function that converts degrees Fahrenheit to Celsius

def fah_to_cel(F):
    temp = F-32
    return temp*(5/9)


# In[9]:


#what does 98.6 degrees convert to?

fah_to_cel(98.6)


# In[10]:


#What does 212 degrees convert to?

fah_to_cel(212)


# One of the points to make about this example is that steps can happen between the 'def' statement and the 'return' statement. In fact, most of the time this is true. (Though it always seems to be 'Pythonic' to do things as tersely as possible - could you rewrite the last function so that there is no intermediate step?)

# $\underline{\hspace{6in}}$
# 
# The last point that we should make today is that sometimes we want to hold onto the output of a function through a variable. We may then possibly use it in another function. Again, there are many ways to represent this, but let me show you one.
# 
# The speed of sound is approximately $331.3 + (0.6 * temp)$ where the temperature is in Celsius.

# In[11]:


#implement a speed of sound function
def speed_of_sound(C):
    return 331.3+0.6*C


# In[12]:


#compute the speed of sound in Jacksonville when it is 
#90 degrees Fahrenheit

C = fah_to_cel(90)

round(speed_of_sound(C),2)


# In[13]:


#Alternative way to define the function to incorporate the conversion.

def speed_of_sound2(F):
    C = fah_to_cel(F)
    return 331.3+0.6*C


# In[14]:


speed_of_sound2(90)


# In[ ]:




