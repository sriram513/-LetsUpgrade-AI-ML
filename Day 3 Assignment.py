#!/usr/bin/env python
# coding: utf-8

# # Question1:
Write a program to subtract two complex numbers in Python.
# In[8]:


a = 5 + 6j
b = 2 - 3j
sub = a - b
print(sub)


# # Question2:
Write a program to find the fourth root of a number.
# In[30]:


number = int(input("enter a number: "))
result = number ** 0.25
print("result:",result)


# # Question3:
Write a program to swap two numbers in Python with the help of a temporary variable.
# In[16]:


a = 4
b = 5
print("Before swaping: a is {}, b is {}".format(a,b))
temp = a
a = b
b = temp
print("After swaping: a is {}, b is {}".format(a,b))


# # Question4:
Write a program to swap two numbers in Python without using a temporary variable.
# In[17]:


a = 4
b = 5
print("Before swaping: a is {}, b is {}".format(a,b))
a,b = b,a
print("After swaping: a is {}, b is {}".format(a,b))


# # Question5:
Write a program to convert Fahrenheit to kelvin and celsius both.
# In[23]:


F = float(input("enter Fahrenheit:"))
C = 5/9 * (F - 32)
K = (F - 32) * 5/9 + 273.15
print("Fahrenheit to kelvin is {}".format(K))
print("Fahrenheit to celsius is {}".format(C))


# # Question6:
Write a program to demonstrate all the available data types in Python. Hint: Use type() function.
# In[29]:


a = 4
print(type(a))
b = 5.0
print(type(b))
c="sriram"
print(type(c))
d = 3 + 7j
print(type(d))
e = True
print(type(e))
f = [1,2,3,4,"sriram",7j]
print(type(f))
g = (1,2,3,4)
print(type(g))
h = {1,2,3}
print(type(h))
i = {1:"sri",2:"ram"}
print(type(i))

