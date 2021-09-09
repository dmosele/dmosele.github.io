#!/usr/bin/env python
# coding: utf-8

# # Comparison, Conjunctions, & Conditionals
# The final thing we need before moving on is the notion of comparison and testing with conditional statements. In a logic course you would understand a conditional statement as something like:
# 
# "**If** the sky is green, **then** 2+2=5"
# 
# Frequently, in coding we want to be able to test multiple conditions such as 
# 
# "**If** the sky is green, **then** 2+2=5. Otherwise, **if** the sky is purple, **then** 3+7=2."
# 
# For the subsequent conditions, the word else or "elif" is frequently used in programming. The difference here is that else is used if none of the earlier conditions are met and elif is used when there are additional conditions are needed.

# In[1]:


# Write a function that takes the month as input and provides the semester as output.
# Month will be an integer that takes a value between 1 and 12

def what_semester(month):
    if month<5 and month>=1:
        return "Spring"
    elif month<8 and month>=5:
        return "Summer"
    elif month<13 and month>=8:
        return "Fall"
    else:
        return "Plz try again"

what_semester(8)


# Note that the above function is a bit imprecise. Frequently, the transition between semesters doesn't happen on the first or last day of the month, so we need to be more granular here.

# In[2]:


# Let's try a similar function with month and day as inputs.

def what_semester2(month,day):
    if (month==1 and day<10) or month==12:
        return "Winter"
    elif month<5 and month>=1:
        return "Spring"
    elif (month<8 and month>=5) or (month==8 and day<16):
        return "Summer"
    elif month<12 and month>=8:
        return "Fall"
    else:
        return "Plz try again"
    
what_semester2(8,20)


# In[3]:


5 != 6


# $\underline{\hspace{6in}}$
# 
# Let's look at another example. This one will be a guessing game. The computer will pick a number between 0 and 9 and you have to guess. It will tell you if your guess is less than, greater than, or spot on the correct value.

# In[4]:


#run this cell only once for each time you play the game
from random import randrange
computer_choice = randrange(10)


# In[5]:


# write a function that allows you to check your guess

def guessing_game(computer_choice,your_guess):
    if your_guess == computer_choice:
        return "Congratulations! You are correct."
    elif your_guess > computer_choice:
        return "You guessed too high"
    else:
        return "You guessed too low"


# In[6]:


guessing_game(computer_choice, 1)


# In[ ]:




