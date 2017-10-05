import os
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps=PorterStemmer()
stop_words=stopwords.words('english')
numbers =['1','2','3','4','5','6','7','8','9','0']
rx=RegexpTokenizer(r'\w+')
k=0;
total=[];
os.chdir('C:\\Users\\DES\\Downloads'+'\\IMDB_reviews\\aclImdb\\train\\neg')
for i in os.listdir(os.getcwd()):
    k=k+1;
    print(k);
    if k>1000:
       break;
    review=open(i,encoding='utf8')
    review=review.read()
    review=review.lower()
    token=rx.tokenize(review);
    token=sorted(token);
    token=[i for i in token if not i in stop_words]
    token=[i for i in token if not i in numbers]
    token=[ps.stem(i) for i in token]
    
    for j in token:
        total.append(j);
total=sorted(total);
##total=[ps.stem(i) for i in total]
i=0;
print(len(total));
#counting frequency of every word
my_dic={};
while i < len(total):
    k=1;
    if i < (len(total)-1):
        while total[i]==total[i+1]:
            k=k+1;
            i=i+1;
            if i >= len(total)-1:
                break;
    my_dic[total[i]]=k;
    i=i+1;
print(len(my_dic));
print(len(set(total)))
