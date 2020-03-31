# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-04-02_b.py
#実行方法：ターミナル上で python3 18B09784-04-02_b.py を実行

import math
import numpy as np

def print_array(array):
    for i in range(len(array)):
        print(''.join(map(str,array[i])))

def sub(ele1,ele2,mod):
    return (ele1-ele2)%mod

def mul(ele1,ele2,mod):
    return (ele1*ele2)%mod

def div(ele1,ele2,mod):
    if ele2 == 0:
        return "error"
    else:
        for i in range(mod):
            if (i*ele2)%mod == ele1:
                return i
                break


print("INPUT: linear_equation_Fp.txt")
with open("linear_equation_Fp.txt") as file:
    lines = file.read().splitlines()

#keep first 2 line in data
data=[]
for i in range(2):
    for j in range(len(lines[i])):
        if lines[i][j]=="=":
            data.append(lines[i][j+1:])
            break
p=int(data[0])
n=int(data[1])

a_ele=[]
for k in range(3,n+3):
    a_ele.append(lines[k][:])

#make A
a=[]
b_ele=[]
for i in range(n):
    ele_a=a_ele[i]
    ele_a_in=[]
    for j in range(len(ele_a)):
        ele_a_in.append(ele_a[j])
    a.append(ele_a_in)

A = np.array(a)
A = A.astype(np.int)


for k in range(n+4,len(lines)):
    b_ele.append(lines[k][:])

#make b
b=[]
for i in range(n):
    ele_b=b_ele[i]
    ele_b_in=[]
    ele_b_in.append(ele_b)
    b.append(ele_b_in)

B = np.array(b)
B = B.astype(np.int)


AB = np.append(A,B,axis=1)
lenAB = len(AB[0])

###

for i in range(n):   #column
    for j in range(i,n): #row
        #if element=0, swap with the lower element
        if AB[j][i] == 0:
            if j == n-1:
                break
            else:
                AB[[j,j+1]]=AB[[j+1,j]]

        #if element not 0, divide all element in row with first number
        if AB[j][i] != 1:
            keep = AB[j][i]
            for k in range(i,lenAB):
                AB[j][k]=div(AB[j][k],keep,p)
#get first element of all row become 1

#make the lower row become 0
    for m in range(i+1,n): #row
        if AB[m][i] != 0:
            for k in range(lenAB):  #add all element in row
                AB[m][k]=sub(AB[m][k],AB[i][k],p)
#until here we get G matix with upper triangular matrix

#make left side to be identity matrix
for i in range(n-1,-1,-1): #column
    for j in range(i):  #row
        deg = AB[j][i]
        for m in range(i,lenAB):
            keep = mul(AB[i][m],deg,p)
            AB[j][m]=sub(AB[j][m],keep,p)

x=AB[:,n].reshape(n,1)

print("OUTPUT:")
print("x=")
print_array(x)
