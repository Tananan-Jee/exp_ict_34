# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-03-03.py
#実行方法：ターミナル上で python3 18B09784-03-03.py を実行

import math
#read file r.txt
print("INPUT: r.txt")
with open("r.txt") as file:
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
for k in range(3,len(lines)-2):
    c.append(lines[k][:])

#get r
r=[]
r=lines[-1][:]

#find distance between c and r
d=[]
for i in range(int(data[1])): #for all c
    count=0
    for j in range(int(data[0])):#compare each element in c with r
        if c[i][j]!=r[j]:
            count+=1
    d.append(count)

print("OUTPUT:")

#find the minimum distance
d_min=data[0]
for i in range(len(d)):
    if int(d[i])<=int(d_min):
        d_min=d[i]
        i_md=i #index of element in c that have minimum distance with r

print("hat_c=" + c[i_md])
print("i_MD=" + str(i_md))
