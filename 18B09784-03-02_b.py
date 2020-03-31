# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-03-02_b.py
#実行方法：ターミナル上で python3 18B09784-03-02_b.py を実行

import math
#read file code.txt
print("INPUT: code.txt")
with open("code.txt") as file:
    lines = file.read().splitlines()

#keep first 2 line in data
data=[]
for i in range(2):
    for j in range(len(lines[i])):
        if lines[i][j]=="=":
            data.append(lines[i][j+1:])
            break
#data[0] = n = length
#data[1] = M = number if element in C

#get C
c=[]
for k in range(3,len(lines)):
    c.append(lines[k][:])

#find distance in any 2 elements then keep in array d
d=[]
for i in range(int(data[1])): #first element
    for k in range(int(data[1])): #second element
        count=0
        if k>i:
            for j in range(int(data[0])):
                if c[i][j]!=c[k][j]:
                    count+=1
            d.append(count)

print("OUTPUT:")
print("d_min=" + str(min(d))) #min(d)=minimum value in d
r=math.log(int(data[1]),2)/int(data[0])
print("R=" + str(round(r,6))) #6 decimal of R , R=log2(m)/n
