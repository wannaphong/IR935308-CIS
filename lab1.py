# -*- coding: utf-8 -*-
# อ่านไฟล์จากที่เราเตรียมไว้ โดยเปิดไฟล์ แล้วอ่านไฟล์เก็บใน docs1
with open("docs1.txt", "r", encoding="utf-8-sig") as file:
    docs1 = file.read().lower() # แปลงให้เป็นตัวพิมพ์เล็ก

with open("docs2.txt", "r", encoding="utf-8-sig") as file:
    docs2 = file.read().lower()

with open("docs3.txt", "r", encoding="utf-8-sig") as file:
    docs3 = file.read().lower()

with open("docs4.txt", "r", encoding="utf-8-sig") as file:
    docs4 = file.read().lower()

with open("docs5.txt", "r", encoding="utf-8-sig") as file:
    docs5 = file.read().lower()

#print(docs1) # แสดงข้อมูลใน docs1
# ใช้คำสั่งนี้เฉพาะครั้งแรกในการใช้งานตัดคำ
#import nltk
#nltk.download('punkt')
####จบ####
# ตัดคำภาษาอังกฤษ
# ex
#จาก "I love cat" -> ["I", "Love", "cat"]
from nltk.tokenize import word_tokenize
list_word_docs1 = word_tokenize(docs1)
# ตัดคำ จากข้อความที่อยู่ใน docs1
list_word_docs2 = word_tokenize(docs2)
# ตัดคำ จากข้อความที่อยู่ใน docs2
list_word_docs3 = word_tokenize(docs3)
list_word_docs4 = word_tokenize(docs4)
list_word_docs5 = word_tokenize(docs5)
# เขียนข้อมูลลงไฟล์
with open('list_d1.txt', 'w', encoding='utf-8') as file:
    file.write(str(list_word_docs1))
# write('เขียนได้เฉพาะ string เท่านั้น') 
# เพราะ list_word_docs1 เป็น list
# ต้องแปลงเป็น string ก่อน
with open('list_d2.txt', 'w', encoding='utf-8') as file:
    file.write(str(list_word_docs2))
    
with open('list_d3.txt', 'w', encoding='utf-8') as file:
    file.write(str(list_word_docs3))
    
with open('list_d4.txt', 'w', encoding='utf-8') as file:
    file.write(str(list_word_docs4))

with open('list_d5.txt', 'w', encoding='utf-8') as file:
    file.write(str(list_word_docs5))
