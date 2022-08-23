#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Find the Factorial of a Number?

# In[7]:


num=int(input("Ente the no to check its factorial"))
factorial=1
#check if no is negative
if num<0:
    print("No foractor for negative no")
if num == 0:
    print("Factorial of 0 is 1")
if num > 0:
    for i in range(1,num+1):
        factorial=i*factorial
    print("The Factorial of",num,"is",factorial)


# 2. Write a Python Program to Display the multiplication Table?

# In[9]:


num=int(input("Enter the no for multiplication Table"))
for i in range(1,num):
    print(num,"=",i,"X",num,"=",num*i)


# 3. Write a Python Program to Print the Fibonacci sequence?

# In[14]:


nterm=int(input("Enter How many terms?"))

n1,n2=0,1
count=0

#check the terms is valid
if nterm <=0:
    print("Please enter a positive interger")
   
elif nterm==1:
    print("Fibbonacci sequence upto",nterm,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterm:
        print(n1)
        nth = n1 + n2
        # update values
        n1=n2
        n2 = nth
        count += 1
        


# 4. Write a Python Program to Check Armstrong Number?

# In[15]:


num = int(input("Enter the no to check for Armstrong no"))
sum=0
temp=num
while temp >0:
    digit = temp % 10
    sum = sum + digit **3
    temp = temp/10
if num==sum:
    print(num,"is the Amstrong no")
else:
    print(num,"is not a Amstrong no")


# 5. Write a Python Program to Find Armstrong Number in an Interval?

# In[25]:


lower = 100
upper= 2000

for num in range(lower,upper +1):
    order = len(str(num))
    sum =0
    temp =num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit **order
        temp//= 10
    if num==sum:
        print(num)


# 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[33]:


num=int(input("Enter the number"))
if num < 0:
    print("Enter the Positive no")
else:
    sum=0
    while num > 0:
        sum= sum + num
        num = num-1
    print("The sum is: ",sum)


# In[ ]:




