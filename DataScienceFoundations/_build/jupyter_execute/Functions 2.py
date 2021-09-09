#!/usr/bin/env python
# coding: utf-8

# # Functions 2
# While we explored some function basics, there are lots more variations of what can happen with functions. For example, functions can have multiple inputs and/or multiple outputs. Frequently, a function has default inputs if not otherwise specified. Let's explore some examples.

# In[1]:


# Write a function that takes two numbers as inputs and adds them

def add_2_numbers(x,y):
    return x+y

z1 = add_2_numbers(2,3)

print(z1)


# This function took the two input numbers and output precisely one number, the sum. Depending on what we want to do with the function and its output, it might not require a return statement at all, but a "pass" statement instead.

# In[2]:


# Let's try a similar function in a different way

def add_nums_badly(x,y):
    print(x+y+1)
    pass

z2 = add_nums_badly(2,3)

print(z2)


# In[3]:


###


# Note that this function doesn't actually return anything! However, there is output of sorts in a print statement.

# $\underline{\hspace{6in}}$
# 
# Let's look at another example. This function will take a string as input and output the string reversed as well as the length of the string. That is, there is one input and two outputs.

# In[4]:


#implement the function described above

def reverse_and_count(word):
    new_word = ''
    n = len(word)
    for i in range(n):
        new_word = new_word + word[n-i-1]
    return new_word, n
    
reverse_and_count('dolphin')


# In[5]:


#apply the function to another string

reverse_and_count('Supercalifragilisticexpialidocious')


# In[6]:


reverse_and_count('string with spaces')


# $\underline{\hspace{6in}}$
# 
# In previous examples we have stored *the* output in a variable. What happens if we try to do that with a function with multiple outputs?

# In[7]:


testing = reverse_and_count('Supercalifragilisticexpialidocious')

print(testing)


# The output of the function is returned in a data type known as a 'tuple'. Here if we want to reference one of the outputs individually, we can do so by grabbing one of the entries kind of like in a list.

# In[8]:


testing[0]


# In[9]:


testing[1]


# However, another way to deal with multiple outputs that you would want to use in the future is to give each output a name and separate them by commas.

# In[10]:


rev_word, len_of_word = reverse_and_count('Supercalifragilisticexpialidocious')


# In[11]:


print(rev_word)


# In[12]:


print(len_of_word)


# $\underline{\hspace{6in}}$
# 
# Your turn! Design a function that has multiple inputs, outputs, or both.

# In[ ]:





# In[ ]:





# In[ ]:




