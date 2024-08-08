#!/usr/bin/env python
# coding: utf-8

# In[1]:


#str is immutable
a=5
print(id(a))
a=10
print(id(a))
b=10
print(id(b))


# In[2]:


#are integers mutable or not 
# other properties of strings
print("_" * 10)


# In[3]:


print('el' in  'Hello')


# In[4]:


print('Hello ' in 'Hello' )


# In[5]:


#Concatenation
str1 = 'Dinesh Kumar'
str2 = 'Dhanush'
conc_str = str1 + str2
print(conc_str)


# In[6]:


#string_Function (Member_fn?)
#str1 = 'Dinesh Kumar'
#isalpha()
#isdigit()
#isalnum,islower,isupper.startswitch('R'),endswitch('n')

str1 = 'Dinesh Kumar'
print(str1.upper())


# In[7]:


print(str1.lower())


# In[8]:


#str1.capitalize(), str1.swapcase(), str1.find('a')
print(str1.replace('a', 'b', 1))


# In[9]:


print(str1.split())


# In[10]:


str1 = 'DineshKumar'
print(str1.split())
print(str1.capitalize())
print(str1.swapcase())
print(str1.find('a'))


# In[11]:


str1 = ','
print(str1.split())


# In[12]:


str1 = 1

print(str1.split())


# In[ ]:


# Partition and Split ?
str1 = 'Dinesh Kumar'
print(str1.partition())


# In[ ]:


# Partition and Split ? 
#split will split the string at any occurrence of the given argument, 
#while partition will only split the string at the first occurrence of the given argument 


# In[ ]:


#Console input and Output
#Console input and output
'''Input
• Input from the keyboard - it’s a string
• use the input( ) function to get from keyboard
• use split( ) to split the input values
• use type conversion functions such as int( ), float( ) etc.'''


# In[ ]:


'''type
int to str and str to int conversion'''


# In[ ]:


a,b = input('enter a and b : ').split()


# In[ ]:


a,b = input('enter a and b : ').split()
print(a + b)
c= int(a) + int (b)
print(c)


# In[ ]:


'''get 3 inputs and split and print each input separately 
float, str, int'''


# In[ ]:


#OUTPUT Statements
#Escape statements used for print statement
'''stdout?'''


# In[ ]:


n,a,s = input('Enter name, age, salary : ').split()
data = n,a,s
name = data[0]
print (name)
#age = data[1]
#salary = data[2]
#print('your name is ' +name + 'age ' +age + 'salary' +salary)


# In[15]:


data = input('Enter name, age, salary : ').split()

name = data[0]
print (name)
age = data[1]
salary = data[2]
print('your name is ' +name + ' age ' +age + ' salary ' +salary)


# In[ ]:





# In[ ]:




