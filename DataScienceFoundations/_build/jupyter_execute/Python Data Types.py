#!/usr/bin/env python
# coding: utf-8

# # Data Types in Python

# While most operations we have used in Python so far have centered around computation with integers or numbers more generally (floating point numbers), Python has several other built-in data types such as strings, lists, tuples, and dictionaries. Let's get started with strings and lists.

# In[1]:


# Assign the word "dolphin" to a variable named string1 and then print the variable
string1 = "dolphin"
print(string1)


# If you want to access a certain character from your string, you can use string_name[k] where string_name is the variable you used and k represents the spot in the string. Note that Python always starts numbering from zero, so string_name[0] would be the first letter of the string.

# In[2]:


# Pick a letter from the word "dolphin" using the technique above
string1[1]


# Interestingly, one can perform an addition operation on strings that can essentially paste them together. Assign strings to two variables and see what happens when you add them together.

# In[3]:


# Combine two strings using +
string2 = "JU "
string2+string1


# Frequently when working with data, for consistency, you need to make words all lower or upper case. You can make a word lower case using the lower() method and upper case using the upper() method. Methods differ from functions as you tack them onto the end of the variable. For example:
# 
# string_name.lower()

# In[4]:


long_string = "On the Banks of the wide St. Johns"
#Make this phrase lower case
long_string.lower()


# $\underline{\hspace{6in}}$

# Lists are really foundational to how things are done in Python and have really special characteristics. Just to get started, a list is just what it sounds like - a collection of objects in a particular order. For example:

# In[5]:


X = [1,'dolphin',3.14159]

print(X)


# Note that I said a list is a collection of objects, not just numbers. A list can even contain a list!

# In[6]:


Y = [2,X,'JU']

print(Y)


# Just like with strings, we can reference a particular element of a list by its position in the list (again, the numbering starts at zero). We would use the same notation to do it. That is,
# 
# list_name[k]
# 
# where list_name is the name of the list, and k is the location of the element. Find the element in the '1' spot of the list X above.

# In[7]:


#Find the element in the '1' spot of X
Y[1][2]


# If you want to tack something on to the end of a list, you can use the append() method where you put the element that you want to add to the list within the parentheses.

# In[8]:


# Add the number 7 to the end of the list X and print out X
X.append(7)
print(X)


# $\underline{\hspace{6in}}$

# The last point that we should make in this section is that if you are ever unsure as to what data type an object represents, just use the type() function to find out.

# In[9]:


type(X)


# In[10]:


type(string1)


# In[11]:


type(3.14159)


# In[12]:


type(2)


# In[ ]:




