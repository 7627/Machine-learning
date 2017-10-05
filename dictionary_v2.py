"""
This code takes a number of text files( reviews) and makes a dictionary which
tells the frequency of each words in the whole text i.e combining all text files
"""

import os
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
os.chdir('C:\\Users\\yamit\\Downloads\\Sentiments_data\\aclImdb\\train\\pos')
foo=''
max_reviews=int(input('How many reviews do you want to analyse?   :'));
j=0;
for i in os.listdir():
    j=j+1
    if j>max_reviews:
        break;
    f=open(i)
    fo=f.read().lower()
    foo=foo+fo;
    

#'\W+'means a pattern with all non-alphanumeric characters. So it will split the text with \W+ as delimiter.
#For more, see Regular expressions in python documentation.
split=re.split('\W+',foo)
split=sorted(split)
a=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
split=[i for i in split if not i in a]
split=[i for i in split if not i in stopwords.words('english')]
ps=PorterStemmer()
stemmed=[ps.stem(i) for i in split]

#counting requency of each words
frequency_counter={}
for i in stemmed:
    frequency_counter[i]=0;
for i in stemmed:
    frequency_counter[i]=frequency_counter[i]+1;

#printing length of dictionary created
print('Total number of words including repetation:  ', len(split), '\n')
print('Number of words in the frequency_counter are: ', len(frequency_counter))
