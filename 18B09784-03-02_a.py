# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-03-02_a.py
#実行方法：ターミナル上で python3 18B09784-03-02_a.py を実行

import math

print("INPUT:")
len=int(input("n="))
m=int(input("M="))
print("C=")
c=[]
for i in range(m):
    ele_c=str(input()) #get
    c.append(ele_c)

#find distance in any 2 elements then keep in array d
d=[]
for i in range(m): #first element
    for k in range(m): #second element
        count=0
        if k>i:
            for j in range(len):
                if c[i][j]!=c[k][j]:
                    count+=1
            d.append(count)

print("OUTPUT:")
print("d_min=" + str(min(d))) #min(d)=minimum value in d
print("R=" + str(round(math.log(m,2)/len,6))) #6 decimal of R , R=log2(m)/n
