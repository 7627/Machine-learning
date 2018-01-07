"""
This code takes a number of text files( reviews) and makes a dictionary which
tells the frequency of each words in the whole text i.e combining all text files and
creates a list with items contaning dictionary of frequency_count of words in training set"""

import os
import nltk
import re
import numpy 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

    
#'\W+'means a pattern with all non-alphanumeric characters. So it will split the text with \W+ as delimiter.
#For more, see Regular expressions in python documentation.
def frequency_count(foo):
    split=re.split('\W+',foo)
    split=sorted(split)
    a=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
    split=[i for i in split if (not i in a) and (not i in stopwords.words('english'))]
    #split=[i for i in split if not i in stopwords.words('english')]
    ps=PorterStemmer()
    stemmed=[ps.stem(i) for i in split]

    #counting requency of each words
    frequency_counter={}
    for i in stemmed:
        frequency_counter[i]=0;
    for i in stemmed:
        frequency_counter[i]=frequency_counter[i]+1;
    return frequency_counter
#printing length of dictionary created

"""Create a database having all the words used in max_reviews
and create a array/list 'frequencies' with every item having dictionary of words in that input
"""


max_reviews=int(input('How many reviews do you want to analyze?   :'));
#frequencies=[]
rating=[];
"""Reading Positive reviews"""
os.chdir('C:\\Users\\yamit\\Downloads\\Sentiments_data\\aclImdb\\train\\pos\\');
j=0;
foo_pos=''
for i in os.listdir():
    j=j+1
    if j>max_reviews:
        break;
    f=open(i,encoding='utf-8')
    print(i+' ')
    rating.append(1);
    fo=f.read().lower()
    #frequencies.append(frequency_count(fo)); #making list of dictionaries
    foo_pos=foo_pos+' '+fo
frequency_pos=frequency_count(foo_pos);

"""Reading negative reviews"""
os.chdir('C:\\Users\\yamit\\Downloads\\Sentiments_data\\aclImdb\\train\\neg\\');
foo_neg=''
j=0;
for i in os.listdir():
    j=j+1
    if j>max_reviews:
        break;
    f=open(i,encoding='utf-8')
    print(i+' ')
    rating.append(0);
    fo=f.read().lower()
    #frequencies.append(frequency_count(fo)); #making list of dictionaries
    foo_neg=foo_neg+' '+fo
frequency_neg=frequency_count(foo_neg);

database=frequency_count(foo_pos+' '+foo_neg)

"""A=[]
j=0;
for i in range(0,len(rating)):
    j=j+1
    if j>len(rating):
        break;
    A.append([])
    for k in database:
        if k in frequencies[j-1]:
            A[j-1].append(frequencies[j-1][k])
        else:
            A[j-1].append(0)
"""

"""A=numpy.matrix(A)
x=numpy.dot(numpy.dot(inv(numpy.dot((A.T),A)),A.T),B)
"""

"""Takes a review as input and return a list with len(y)=len(database) and items are the
frequencies of words from database in the given input"""
"""def my_review(x):
    x=frequency_count(x);
    y=[];
    for k in database:
        if k in x:
            y.append(x[k])
        else:
            y.append(0)
    return y
"""
"""calulates ..., where X is the input list for which prediction is to be done"""
"""def naive_bayes(A,X,rating):
    #calculates combined_prob of 0 and 1
    prob=[]
    k=0;
    for i in rating:
        if i==1:
            k=k+1;
    #probability for 1

    total_words=0;
    for i in range(0,len(X)):
        prob.append(0);
        for j in range(0,len(rating)):
            if rating[j]==1:
                prob[i]=prob[i]+A[j][i];
                total_words=total_words+A[j][i];
              #  if A[j][i]==X[i]
            #     prob[i]=prob[i]+1;
    
  #  prob=[(i+1)/(total_words+len(X)) for i in prob]
    prob_1=k/len(rating)
    combined_prob=1;
    for i in prob:
        combined_prob=combined_prob*i;
    combined_prob=combined_prob*prob_1;
    return prob,combined_prob,prob_1,total_words;
"""
prob_pos={}
prob_neg={}
combined_prob_pos=1;
combined_prob_neg=1;
pos_words=0
neg_words=0;
for i in frequency_pos:
    pos_words=pos_words+frequency_pos[i];
for i in frequency_neg:
    neg_words=neg_words+frequency_neg[i];

for i in database:
    if i in frequency_pos:
        prob_pos[i]=(frequency_pos[i]+1)/(pos_words+len(database))*1000
    else:
        prob_pos[i]=1/(pos_words+len(database))*1000
    if i in frequency_neg:
        prob_neg[i]=(frequency_neg[i]+1)/(neg_words+len(database))*1000
    else:
        prob_neg[i]=1/(neg_words+len(database))*1000

prob_1=0; prob_0=0;
for i in rating:
    prob_1=prob_1+i;
prob_1=prob_1/len(rating);
prob_0=1-prob_1;

numpy.save('C:\\Users\\yamit\\Downloads\\Sentiments_data\\prob_pos.npy',prob_pos)
numpy.save('C:\\Users\\yamit\\Downloads\\Sentiments_data\\prob_neg.npy',prob_neg)

def predict(x,prob_pos,prob_neg,prob_1,prob_0):
    x=frequency_count(x);
    pos=1;
    neg=1;
    for i in x:
        if i in prob_pos:
            pos=pos*pow(prob_pos[i],x[i]);
        if i in prob_neg:
            neg=neg*pow(prob_neg[i],x[i]);
    pos=pos*prob_1;
    neg=neg*prob_0;
    if pos>neg:
        #print('Positive');
        return 1;
    elif neg>pos:
        #print('Negative')
        return 0
    else:
        print("pos=",pos)
        print('neg=',neg)
        return "don't know"


def accuracy(prob_pos,prob_neg,prob_1,prob_0,rating):
    result=[];
    test=[];
    test_reviews=int(input('How many review you need for testing? :  '))
    j=0;
    os.chdir("C:\\Users\\yamit\\Downloads\\Sentiments_data\\aclImdb\\test\\pos\\")
    for i in os.listdir():
        j=j+1;
        if j>test_reviews:
            break;
        f=open(i,encoding='utf-8');
        f=f.read().lower()
        test.append(1);
        result.append(predict(f,prob_pos,prob_neg,prob_1,prob_0))
    j=0;
    os.chdir("C:\\Users\\yamit\\Downloads\\Sentiments_data\\aclImdb\\test\\neg\\")
    for i in os.listdir():
        j=j+1;
        if j>test_reviews:
            break;
        f=open(i,encoding='utf-8');
        f=f.read().lower()
        test.append(0)
        result.append(predict(f,prob_pos,prob_neg,prob_1,prob_0))
    accrcy=0;
    for i in range(0,len(result)):
        accrcy=accrcy+(result[i]==test[i])
    return accrcy/len(result)*100,accrcy,result

    
#print('Classification accuracy is',accuracy(prob_pos,prob_neg,0.5,0.5,rating)[0])
#print('Total number of words including repetation:  ', len(split), '\n')
#print('Number of words in the frequency_counter are: ', len(frequency_counter))
