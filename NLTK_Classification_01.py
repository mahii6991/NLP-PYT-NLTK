#!/usr/bin/env python
# coding: utf-8

# # NLP Basics: What is Natural Language Processing & the Natural Language Toolkit?

# ### How to install NLTK on your local machine
# 
# Both sets of instructions below assume you already have Python installed. These instructions are taken directly from [http://www.nltk.org/install.html](http://www.nltk.org/install.html).
# 
# **Mac/Unix**
# 
# From the terminal:
# 1. Install NLTK: run `pip install -U nltk`
# 2. Test installation: run `python` then type `import nltk`
# 
# **Windows**
# 
# 1. Install NLTK: [http://pypi.python.org/pypi/nltk](http://pypi.python.org/pypi/nltk)
# 2. Test installation: `Start>Python35`, then type `import nltk`

# ### Download NLTK data

# In[1]:


import nltk
nltk.download()


# In[2]:


dir(nltk)


# ### What can you do with NLTK?

# In[3]:


#these are the stopwords that being used in the dictionary

from nltk.corpus import stopwords

stopwords.words('english')[0:500:50]


# In[4]:


#read the text data with the help of the tsv file in the dataset
#so the best way to read is in the juypter notebook, because it is not being read in this form the google colab
rawData = open("SMSSpamCollection.tsv").read()


# In[5]:


#print the raw data
rawData[0:500]


# In[6]:


parsedData = rawData.replace('\t', '\n').split('\n')


# In[7]:


parsedData[0:7]


# In[8]:


labelList = parsedData[0::2]#finding out the label of the text dataset
#by this function we means that start from the o and go to the end and split it by 2
textList = parsedData[1::2]#finding out the text of the text document
#in this way we are splitting the whole list and taking the valus of the 2 in the secound position


# In[9]:


print(labelList[0:5])
print(textList[0:5])


# In[10]:


import pandas as pd

#now we are making the dataset form the dataset that we have seperated in the previous example
fullcorpus = pd.DataFrame({
    'label' : labelList,
    'body_list' : textList
})

fullcorpus.head()


# In[11]:


print(len(labelList))
print(len(textList))


# In[12]:


print(labelList[-5:])
#there is the last one that is irrelavant to the model 
#and that entry is creating the problem in making the dataframe


# In[13]:


import pandas as pd

#now we are making the dataset form the dataset that we have seperated in the previous example
fullcorpus = pd.DataFrame({
    'label' : labelList[:-1],
    'body_list' : textList
})

fullcorpus.head()


# In[14]:


fullcorpus = pd.read_csv("SMSSpamCollection.tsv", sep="\t",header= None)
fullcorpus.head()


# In[15]:


#now that is the joke what
#I have done in the past couple of code can be done with the one line of code


# In[16]:


fullcorpus.columns = ['label','body_list']

fullcorpus.head()


# In[17]:


#finding out what is the shape of the dataset
fullcorpus.shape


# In[18]:


print("Input data has {} rows and {} column".format(len(fullcorpus),len(fullcorpus.columns)))


# In[19]:


#find out how many are spam and how many are not spam
print("Out of {} rows, {} are spam, {} are ham".format(len(fullcorpus),
                                                      len(fullcorpus[fullcorpus['label']=='spam']),
                                                      len(fullcorpus[fullcorpus['label']=='ham'])))


# In[24]:


#finding out how much missing data is present there!!!
print("number of null in label:{}".format(fullcorpus['label'].isnull().sum()))
#finding the number of null value in both the column
print("number of null in text:{}".format(fullcorpus['body_list'].isnull().sum()))


# In[ ]:


#what is the regular experssion ..?
#so the regular expression is the set of numbers which retrun the similar text 
#so 'nlp' will return the nlp and the '[j-q]+' will retrun the numbers between the j and q 
#and same with the [j-q] will return the similar text between this two texts


# # Learning how to use the regular expression

# In[28]:


#using regular expression in python

import re

re_test = 'This is a made up string to test 2 different regex methods'
re_test_messy = 'This      is a made up     string to test 2    different regex methods'
re_test_messy1 = 'This-is-a-made/up.string*to>>>>test----2""""""different~regex-methods'


# In[29]:


re.split('\s',re_test)#we are splitting the text wiht the whitespace that is present between the text.


# In[31]:


re.split('\s',re_test_messy)#the same process we will going to do it here


# In[32]:


re.split('\s+',re_test_messy)#the same process we will going to do it here,but wiht the plus sign that will not going to read the blank spaces


# In[33]:


re.split('\s+',re_test_messy1)#as there is no white space in this text


# In[34]:


re.split('\W+',re_test_messy1)#this allows us to ignore the extra number of characters form the string that we have


# In[36]:


re.findall('\S+',re_test)#here we are using the different methods to find the blank space and to sepreate it with it.


# In[37]:


re.findall('\S+',re_test_messy)#here we are using the different methods to ignore the space in the column


# In[38]:


re.findall('\S+',re_test_messy1)


# In[39]:


re.findall('\w+',re_test_messy1)


# In[ ]:


#the takeaways will be two things from this first we have used the findall and 
#secound we have used the split for the purpose of tokenization.
#anything that is based on '\w is based on words'
#anything that is based on '\s' is based on whitespaces.


# # Replacing a specific string

# In[41]:


pep8_test = 'I try to follow PEP8 guidelines'
pep7_test = 'I try to follow PEP7 guidelines'
peep8_test = 'I try to follow PEEP8 guidelines'


# In[42]:


re.findall('[a-z]+',pep8_test)


# In[43]:


re.findall('[A-Z]+',pep8_test)


# In[44]:


re.findall('[A-Z]+[0-9]+',pep8_test)


# In[45]:


re.findall('[A-Z]+[0-9]+',pep7_test)#testing on different statement


# In[46]:


re.findall('[A-Z]+[0-9]+',peep8_test)


# In[47]:


re.sub('[A-Z]+[0-9]+','PEEP8 pthon styleguide',pep8_test)


# # other example of regex methods

# In[ ]:


#re.search()
#re.match()
#re.fullmatch()
#re.escape()


# In[ ]:




