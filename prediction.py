import os
import numpy
import re,nltk
from numpy.linalg import inv 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

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

"""prob_pos and prob_neg are two saved dictionary calculated by dictionary_v2.py
Prob_pos contains dictionary of all words from positive training set
prob_neg contains dictioanry of all words from negative training set
"""
prob_pos=numpy.load('C:\\Users\\yamit\\Downloads\\Sentiments_data\\prob_pos.npy').item()
prob_neg=numpy.load('C:\\Users\\yamit\\Downloads\\Sentiments_data\\prob_neg.npy').item()

while True:
    no_of_reviews=input('How many reviews do you want to test?  : ')
    try:
        no_of_reviews=int(no_of_reviews)
        break;
    except ValueError:
        print("Your input is expected to be a  number")
    
for i in range(1,no_of_reviews+1):
    if i==11:
        x=input('Enter your 11th review :  ')
    elif i==12:
        x=input('Enter your 12th review :  ')
    elif i%10==1:
        x=input('Enter your '+str(i)+'st review :  ')
    elif i%10==2:
        x=input('Enter your '+str(i)+'nd review :  ')
    else:
        x=input('Enter your '+str(i)+'th review :  ')
    result=predict(x,prob_pos,prob_neg,0.5,0.5)
    if result==1:
        print('Positive')
    elif result==0:
        print('Negative')
    else:
        print("I am learning, I am sorry that I can't help you with this one!")


    
