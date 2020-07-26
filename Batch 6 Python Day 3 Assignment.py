#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Sum of n numbers with help of while loop 

#Input from user
num = eval(input("Please enter the number "))
sum = 0
while num >0:
    sum = sum + num
    print(f"Number is --> {num} Sum is --> {sum}")
    num= num -1
print ("Final Sum is ", sum)
print (f"Final Sum is  {sum}")
print ("Final Sum is%4d"%(sum))
    


# In[66]:


# Take a number and find whether it is prime or not

# Input from user
num = int(input("Enter a number "))

# prime numbers are greater than 1
if num > 1:
    
    # Check starting from 2 till number, increment by 1 
   for each in range(2,num):
       if (num % each) == 0:
           print(f"{num} is not a prime number!")
           break
   else:
       print(f"{num} is a prime number!")
       
# input number is less than or equal to 1
else:
   print(f"{num} is not a prime number!")

