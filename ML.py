# 0 is left, 1 is right
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

def lv_number(a, b):
   string1 = a
   string2 = b
   distance = 0
   n1 = len(string1)
   n2 = len(string2)
   
   if n1 >= n2:
       for i in range(n1):
           if i < n2:
               if string1[i] != string2[i]:
                   distance += 1
           else:
               distance += 1
   else:
       for i in range(n2):
           if i < n1:
               if string2[i] != string1[i]:
                   distance -= 1
           else:
               distance -= 1
   
   
       
   return distance

file = open('Healthcare1.csv', 'r')
text = file.readlines()
for i in range(len(text)):
	text[i]=text[i].strip('\n')
lst = []
for i in text:
	lst.append(i.split(','))
target = []
find = []
for i in lst:
	find.append(i[0])
	target.append(i[1])
file.close()
vectorizer = CountVectorizer()
vectorizer.fit(find)

vector = vectorizer.transform(find)

clf = MultinomialNB().fit(vector, target)

test = open('HealthCareTest.csv', 'r').readlines()
test = test[1:]


vector2 = vectorizer.transform(test)

predicted = clf.predict(vector2)

left = []
right = []
for i in range(len(predicted)):
	if predicted[i] == '1':
		right.append(test[i])
	elif predicted[i] == '0':
		left.append(test[i])
counter = 0
for i in left:
	for k in left:
		if k != i:
			counter += lv_number(k, i)
counter2 = 0
for i in right:
	for k in right:
		if k != i:
			counter2 += lv_number(k, i)
print('left right')
print(counter/len(left), counter2/len(right))
print(len(left), len(right))
print(str(len(left)) +  ' : ' + str(len(right)))







