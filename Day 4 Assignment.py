#!/usr/bin/env python
# coding: utf-8

# # Question1:
Research on whether addition, subtraction, multiplication, division, floor division, and modulo operations
be performed on complex numbers. Based on your study, implement a Python program to demonstrate
these operations.
# In[29]:


a = 5 + 5j
b = 3 - 10j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#complex numbers doesnot satisfies the floor division
# a // b gives an error
#complex numbers doesnot satisfies the module operation
# a % b gives an error
 


# # Question2:
Research on range() functions and its parameters. Create a markdown cell and write in your own words
(no copy-paste from google please) what you understand about it. Implement a small program of your
choice on the same.range() is the inbuit function in python.range() syntax is "range(start,stop,steps)" Mainly this range is useful to print numbers from whatever range you want along with the starting number to ending number.you can also print negative range also.By default range() function starts from 0.
# In[15]:


for i in range(1,5):
    print(i)


# In[18]:


for i in range(0,-5,-1):
    print(i)


# In[21]:


for i in range(5,21,5):
    print(i)


# # Question3:
Consider two numbers. Perform their subtraction and if the result of subtraction is greater than 25, print
their multiplication result else print their division result.
# In[12]:


a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = a-b
if c > 25:
    print(a*b)
else:
    print(a/b)


# # Question4:
Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the result as
"square of that number minus 2".
# In[24]:


list = [1,12,3,4,15,26,7,8,92,10]
for i in list:
    if i % 2 == 0:
        print("square of that number minus 2 is {}".format((i ** 2)-2))


# # Question5:
Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that number
is divided 2.
# In[9]:


list = [1,12,3,4,15,26,7,8,92,10]
for i in list:
    if i > 7 and i % 2 == 0:
        print(i)

