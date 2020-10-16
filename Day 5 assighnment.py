#!/usr/bin/env python
# coding: utf-8

# # Question 1
# write a python program to find the first 20 non even prime natural number

# In[8]:


for i in range(1,21):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)


# # Question 2
# write a python program to implement 15 functions of string

# In[33]:


a='hello world'
print(a.capitalize())
print(a.upper())
print(a.swapcase())
print(a.title())
str="w"
print(a.count(str))
print(a.count('l'))
print(a.count('l',0,6))
print(a.isupper())
print(a.islower())
print(a.isalpha())
print(a.isnumeric())
print(a.isalnum())
print(a.rjust(15))
print(a.rjust(15,"*"))
print(a.ljust(15,"*"))


# # Question 3
# write a python program to check if the given string is a palindraome or anagaram or none of them.
# Display the message according to the use

# # Questionn 4
# write a python user defined functions that removes all the additional characters
# from the string and convert it finally to lower case using built-in lower(). 
# eg: if the string is "DR. Darshan ingle@AIML TRainer", 
#     the output be "drdarshaningleaimltrainer"

# In[ ]:


def abc():
    

