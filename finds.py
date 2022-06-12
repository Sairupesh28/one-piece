import csv
A=[]
with open('enjoysport.csv',newline="") as csvfile:
  for row in csv.reader(csvfile):
    A.append(row)
S = ['Null' for k in range(len(A[0])-1)]
c=0
for row in A[1:]:
  print("h",c," : ",S,sep='')
  c+=1
  if row[-1]=='No':
    continue
  for k in range(len(row)-1):
    if S[k]=='Null':
      S[k]=row[k]
      continue
    if S[k]=='?':
      continue
    if S[k]!=row[k]:
      S[k]='?'
print("h",c," : ",S,sep='')
print("Most specific hypothesis : ",S)