#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#According to provided problem let assume we have tweets in tweet.txt file. So we are going to find out degree of profanity
#for each sent
#set of in appropriate words
racial_slurs={'idiot','ceature','fatty'}
#Importing Regular expression module
import re 
f=open("tweet.txt",'r')
#variable sum
summ=0
#reading tweet file
for i in f: 
#extracting each line using for loop
    print(i,end="")
#separating the line into different words and adding it to list of name words
    words=re.findall(r'\w+',i.lower())
#iterating words in loop
    for i in words:
        for j in racial_slurs:
            #if word of line is present in racial_slur then summ will increase by 1
            if i==j:
                summ=summ+1
    #formula used to find out degree_of_profanity
    degree_of_profanity=summ/len(words)
    print("Degree Of Profanity is: ",degree_of_profanity)
print()

#Thanks and Regards,
#Rajiv Mandade.
#email=rajivmandade13@gmail.com

