# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-03-05_a.py
#実行方法：ターミナル上で python3 18B09784-03-05_a.py を実行

import math
import numpy as np

def plus(array1,array2):
    array=[]
    for i in range(len(array1)):
        array_ele=(int(array1[i])+int(array2[i]))%2
        array.append(array_ele)
    return array

def mul_array(array1,array2):
    array=[]
    row_num=len(array1)
    col_num=len(array2[0])
    mid=len(array2)
    for i in range(row_num):
        array_row=[]
        for j in range(col_num):
            get=0
            for s in range(mid):
                keep=int(array1[i][s])*int(array2[s][j])
                get=(get+keep)%2
            array_row.append(str(get))
        array.append(array_row)
    return array

#factorial
def fact(n):
    if n==0:
        return 1
    else:
        re = 1
        for i in range(2,n+1):
            re = re * i
        return re

#nCr(n,r) n choose r
def nCr(n,r):
    return (fact(n)/(fact(r)*fact(n-r)))



print("INPUT:")
n=int(input("n="))
k=int(input("k="))
print("G=")

g=[]
for i in range(k):
    ele_g=str(input())
    ele_g_in=[]
    for j in range(len(ele_g)):
        ele_g_in.append(ele_g[j])
    g.append(ele_g_in)
G_ori=np.array(g)
G=G_ori[:]


#make all u (2^k)
u_ele=[]
for i in range(2**k):
    x=str(bin(i)[2:]) #change base 10 number to binary
    if len(x)<k: #if length of converted binary less than n add "0" in front
        for j in range(k-len(x)):
            x="0"+x
    x=x[::-1]
    u_ele.append([x])
u_g=np.array(u_ele)

#make 情報ベクトル c=uG
c_g=[]
for i in range(len(u_g)):
    c_g.append(mul_array(u_g[i],G))

#ハミング重み
w_a=[]
for i in range(len(c_g)):
    count=0
    for j in range(n):
        if c_g[i][0][j]!='0':
            count+=1
    w_a.append(count)

A_w=[0]*(n+1)
X_a=[0]*(n+1)

#find A_0(number of element that w=0),A_1,A_2,..
for i in range(n+1):
    A_w[i]=w_a.count(i)

#A(X,Y)
print("A(X,Y)=")
count=0
for i in range(n+1):
    if A_w[i] != 0: #for terms that coefficient are not '0'
        count=count+1
        if A_w[i] == 1: #if coefficient = 1, print x^3 instead of 1x^3
            if count==1: #if it is the first term, print x^3 instead of +x^3
                print("X^" + str(n-i),end="")
                X_a[n-i] = X_a[n-i] + 1
            else:
                print(" + " + "X^" + str(n-i) + "Y^"+ str(i),end="")
                X_a[n-i] = X_a[n-i] + 1
        else:
            if count==1:
                print(str(A_w[i]) + "X^" + str(n-i),end="")
                X_a[n-i] = X_a[n-i]+A_w[i]
            else:
                print(" + " + str(A_w[i]) + "X^" + str(n-i) + "Y^"+ str(i),end="")
                X_a[n-i] = X_a[n-i]+A_w[i]
print("")


#B(X,Y) = (1/|c|)*A(X+Y,X-Y)
#ex. coefficient* X^3Y^7 = coefficient* (X+Y)^3(X-Y)^7
B_w=[0]*(n+1)
for i in range(n+1):
    keep_ele=[0]*(n+1)
    if X_a[i] != 0: #for terms that coefficient are not '0'
        keep_front=[0]*(n+1)
        keep_back=[0]*(n+1)
        for j in range(i+1): #from ex. make (X+Y)^3
            keep_front[j] = nCr(i,i-j)
        for k in range(n-i+1): #from ex. make (X-Y)^7
            keep_back[k] = nCr(n-i,n-i-k)*((-1)**(n-i-k))
        for s in range(i+1): #from ex. make (X+Y)^3(X-Y)^7
            for f in range(n-i+1):
                keep_ele[s+f] = keep_ele[s+f] + keep_front[s]*keep_back[f]
        for x in range(n+1): #from ex. coefficient* (X+Y)^3(X-Y)^7
            B_w[x] = B_w[x] + X_a[i]*keep_ele[x]


num=len(c_g) #number of element in c = 2^k
for i in range(n+1):
    B_w[i]=int(B_w[i]/num)

#B(X,Y)
print("B(X,Y)=")
count=0
for i in range(n,-1,-1):
    if B_w[i] != 0: #for terms that coefficient are not '0'
        count=count+1
        if B_w[i] == 1: #if coefficient = 1, print x^3 instead of 1x^3
            if count==1: #if it is the first term, print x^3 instead of +x^3
                print("X^" + str(i),end="")
            else:
                print(" + " + "X^" + str(i) + "Y^"+ str(n-i),end="")
        else:
            if count==1:
                print(str(B_w[i]) + "X^" + str(i),end="")
            else:
                print(" + " + str(B_w[i]) + "X^" + str(i) + "Y^"+ str(n-i),end="")

print("")
