import numpy
import pandas
import csv
Train = []
Test = []
clstr = []
clstt = []
count = 0
with open('iris.csv',newline="") as csvfile :
  for row in csv.reader(csvfile):
    if count==0:
      count=1
      continue
    if count%3==0 :
      Train.append(row[:-1])
      clstr.append(row[-1])
    else:
      Test.append(row[:-1])
      clstt.append(row[-1])
    count+=1

def dist(a,b):
  import math
  n = len(a)
  d=0
  for j in range(n):
    d+=(float(b[j])-float(a[j]))**2
  return math.sqrt(d)
def myfunc(a):
  return a[0]

testdata = [7.2,3.6,5.1,2.5]
dis = []

for r in range(len(Train)):
  h = Train[r]
  dis.append([dist(h,testdata),clstr[r]])

dis = sorted(dis,key=myfunc)[:5]

freq = {}
for row in dis:
  freq[row[1]]=freq.get(row[1],0)+1

for key in freq.keys():
  predicted = key
  break
for key in freq.keys():
  if freq[predicted]<freq[key]:
    predicted = key

print("Prediction : ",predicted)