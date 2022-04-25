#!/usr/bin/env python
# coding: utf-8

# In[1]:


#first downloading the nltk which is famous for the text analytics
import nltk
nltk.download()


# In[2]:


#uploading all the text form it
from nltk.book import *


# In[4]:


#providing the simple argument to it to find the text of the dataset
text1


# In[5]:


text2


# In[6]:


#it helps to find the context of the word 
text1.concordance("monstrous")


# In[7]:


text3.concordance("lived")


# In[8]:


#next function is to find the common context of two or more words that are used in the sentence
text2.common_contexts(["monstrous","very"])


# In[11]:


#lets find out what is the text 4 about
text4


# In[12]:


#so it is about the inaugraul address ,lets find out its len
len(text4)


# In[13]:


#lets try to generate some random words from it
text4.generate()


# In[15]:


#lets find out some common context from it
text4.common_contexts(["democracy","freedom"])#didn;t got any clear results


# In[10]:


#will try to plot the dispersion plot to check out the words and the contexts of the words before and after results
text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])


# In[16]:


#lets do some more analysis in this text
sorted(set(text4))


# In[17]:


#finding out the length of the sorted set4, so this is the length of distint words that is not used commonly 
len(set(text4))


# In[19]:


#now calculate the measure of lexical richness of the text
from __future__ import division
len(text4)/len(set(text4))
#it means that each word is used 15 times


# In[20]:


text4.count("democracy")


# In[21]:


text4.count("America")


# In[22]:


text4.count("freedom")


# In[24]:


#now lets try to calculate the percentage of it in the text
100*text4.count("freedom")/len(text4)


# In[27]:


#so writing the function for the above manupulation on the dataset
#this function is defined to find the lexical diversity of the function
def lexical_diversity(text):
    return len(text)/len(set(text))


# In[28]:


#we will define another function to find the percentage of the word in the text
def percentage(count, total):
    return 100*count/total


# In[30]:


lexical_diversity(text4)


# # A closer look at python: texts as lists of words

# In[31]:


#defining a list in the python
sent1 = ['call','me','mahii','.']


# In[32]:


sent1


# In[33]:


sent1[1]


# In[34]:


sent1[1:3]


# In[35]:


len(sent1)


# In[36]:


lexical_diversity(sent1)


# In[37]:


sent2 = ['the','family','of','dashwood','had','long','been','settled','in','essex']


# In[38]:


len(sent2)


# In[39]:


#arranged the words according to the dictionary
sorted(sent2)


# In[40]:


len(set(sent2))


# In[41]:


set(sent2)


# In[42]:


sent2.count("essex")


# In[43]:


#adding the list or concatenating the list
sent1 + sent2


# In[44]:


sent1.append("hey")


# In[45]:


sent1


# In[46]:


#lets try out some indexing in the lists
text4[320]


# In[47]:


#providing the multiple argument in the list
text4[320:325]


# In[48]:


#so what we did on the upper section is called the slicing 
#let do it on some more text 
text6[1600:1625]


# In[49]:


sent1[1:]


# In[52]:


#saving into another variable
vocab = set(text4)


# In[54]:


vocab_size = len(text4)
vocab_size


# In[56]:


#we can also use the join and split function on our strings
name = 'Monty' + 'pyton'
name


# # computing with language: simple statistics

# In[57]:


saying = ['After','all','is','said','and','done','more','is','said','than','done']


# In[59]:


tokens_1 = set(saying)
tokens = sorted(tokens_1)

#finding the righ order of the tokens
tokens
#now I get it what does they mean by the richness of the language as we can see that the set function only present the tokens
#that are not repeated in the language. so if 'is' is written twice in our text the set will count it as the one.


# In[60]:


tokens[-2:] #it start counting form the backside


# In[62]:


#finding out the frequency distribution
fdist1 = FreqDist(text4)
fdist1


# In[ ]:




