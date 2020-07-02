#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a python program to sum all the items in a list.

# In[1]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# ## 2.Write a Python program to create a list of empty dictionaries.

# In[2]:


n = 5
l = [{} for _ in range(n)]
print(l)


# ## 3.Write a Python program to access dictionary keys element by index.

# In[3]:


num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])


# ## 4.Write a Python program to iterate over dictionaries using for loops

# In[4]:


d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])


# ## 5.Write a Python program to sum all the items in a dictionary.

# In[5]:


my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))


# ## 6.Write a Python script to concatenate following dictionaries to create a new one.
# ### Sample Dictionary :
# ### a. dic1={1:10, 2:20}
# ### b. dic2={3:30, 4:40}
# ### c. dic3={5:50,6:60}
# ### Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# In[6]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

