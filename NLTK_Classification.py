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

# In[ ]:


import nltk
nltk.download()


# In[ ]:


dir(nltk)


# ### What can you do with NLTK?

# In[ ]:


#these are the stopwords that being used in the dictionary

from nltk.corpus import stopwords

stopwords.words('english')[0:500:50]


# In[ ]:


#read the text data with the help of the tsv file in the dataset
#so the best way to read is in the juypter notebook, because it is not being read in this form the google colab
rawData = open("SMSSpamCollection.tsv").read()


# In[ ]:


#print the raw data
rawData[0:500]


# In[ ]:


parsedData = rawData.replace('\t', '\n').split('\n')


# In[ ]:


parsedData[0:7]


# In[ ]:


labelList = parsedData[0::2]#finding out the label of the text dataset
#by this function we means that start from the o and go to the end and split it by 2
textList = parsedData[1::2]#finding out the text of the text document
#in this way we are splitting the whole list and taking the valus of the 2 in the secound position


# In[ ]:


print(labelList[0:5])
print(textList[0:5])


# In[ ]:


import pandas as pd

#now we are making the dataset form the dataset that we have seperated in the previous example
fullcorpus = pd.DataFrame({
    'label' : labelList,
    'body_list' : textList
})

fullcorpus.head()


# In[ ]:


print(len(labelList))
print(len(textList))


# In[ ]:


print(labelList[-5:])
#there is the last one that is irrelavant to the model 
#and that entry is creating the problem in making the dataframe


# In[ ]:


import pandas as pd

#now we are making the dataset form the dataset that we have seperated in the previous example
fullcorpus = pd.DataFrame({
    'label' : labelList[:-1],
    'body_list' : textList
})

fullcorpus.head()


# In[ ]:


fullcorpus = pd.read_csv("SMSSpamCollection.tsv", sep="\t",header= None)
fullcorpus.head()


# In[ ]:


#now that is the joke what
#I have done in the past couple of code can be done with the one line of code


# In[ ]:


fullcorpus.columns = ['label','body_list']

fullcorpus.head()


# In[ ]:


#finding out what is the shape of the dataset
fullcorpus.shape


# In[ ]:


print("Input data has {} rows and {} column".format(len(fullcorpus),len(fullcorpus.columns)))


# In[ ]:


#find out how many are spam and how many are not spam
print("Out of {} rows, {} are spam, {} are ham".format(len(fullcorpus),
                                                      len(fullcorpus[fullcorpus['label']=='spam']),
                                                      len(fullcorpus[fullcorpus['label']=='ham'])))


# In[ ]:


#finding out how much missing data is present there!!!
print("number of null in label:{}".format(fullcorpus(fullCorpus['label'].isnull())))


# In[ ]:




