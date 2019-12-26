# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:46:00 2019

@author: วรรณพงษ์ ภัททิยไพบูลย์
"""

with open('list_d1.txt', 'r', encoding='utf-8-sig') as file:
    list_w1 = eval(file.read())
    # eval คำสั่งรันโค้ด python จาก string 
    # "[1,2,3]" (str) -> [1,2,3]
    # python code (list)
    # data type to list_w1

py = "print(6+1)"
#eval(py) # str to python code
# output : 7

with open('list_d2.txt', 'r', encoding='utf-8-sig') as file:
    list_w2 = eval(file.read())

with open('list_d3.txt', 'r', encoding='utf-8-sig') as file:
    list_w3 = eval(file.read())

with open('list_d4.txt', 'r', encoding='utf-8-sig') as file:
    list_w4 = eval(file.read())

with open('list_d5.txt', 'r', encoding='utf-8-sig') as file:
    list_w5 = eval(file.read())

"""
Stemming
"""

from nltk.stem.porter import * # เอามาทั้งหมด
stemmer = PorterStemmer()
stem_list_w1 = [stemmer.stem(i) for i in list_w1]
# s = [i for in list]
# เป็น for แบบย่อ เขียนเต็มได้แบบนี้
# s = []
# for i in list:
#  s.append(i)
stem_list_w2 = [stemmer.stem(i) for i in list_w2]
stem_list_w3 = [stemmer.stem(i) for i in list_w3]
stem_list_w4 = [stemmer.stem(i) for i in list_w4]
stem_list_w5 = [stemmer.stem(i) for i in list_w5]
#print(list_w1[:5], stem_list_w1[:5])

"""
Lemmatization
ใช้ WordNet ช่วย
"""
import nltk
nltk.download('wordnet')# สำหรับใช้ครั้งแรก

from nltk.stem import WordNetLemmatizer

# Init the Wordnet Lemmatizer
lem = WordNetLemmatizer()
lem_list_w1 = [lem.lemmatize(w) for w in stem_list_w1]
lem_list_w2 = [lem.lemmatize(w) for w in stem_list_w2]
lem_list_w3 = [lem.lemmatize(w) for w in stem_list_w3]
lem_list_w4 = [lem.lemmatize(w) for w in stem_list_w4]
lem_list_w5 = [lem.lemmatize(w) for w in stem_list_w5]
print(list_w5[:5])
print(stem_list_w5[:5])
print(lem_list_w5[:5])













"""
StopWord

ex =>
i
me
my
myself
we
our
ours
"""
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
st= stopwords.words('english')
s_word1 = [word for word in lem_list_w1 if word not in st]
s_word2 = [word for word in lem_list_w2 if word not in st]
s_word3 = [word for word in lem_list_w3 if word not in st]
s_word4 = [word for word in lem_list_w4 if word not in st]
s_word5 = [word for word in lem_list_w5 if word not in st]

# ToDo:
# index
