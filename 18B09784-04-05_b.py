# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-04-05_b.py
#実行方法：ターミナル上で python3 18B09784-04-05_b.py を実行

import math
import numpy as np

def print_array(array):
    for i in range(len(array)):
        print(''.join(map(str,array[i])))

def add(array1,array2):
    array=''
    x=''
    for i in range(1,len(array1)-1):
        if array1[i] != "[" or array1[i] != "]":
            array = array + str((int(array1[i])+int(array2[i]))%2)
    x= "[" + array + "]"
    return x


def mul(array1,array2,f,len_f,deg):
    #normal multiply
    array=np.zeros(2*deg-1)
    for i in range(1,len(array1)-1):
        for j in range(1,len(array2)-1):
            array[i+j-2]=(array[i+j-2]+(int(array2[j])*int(array1[i])))%2
    #find remainder
    array=array[::-1] #get result of array1*array2
    f=f[::-1] #reverse f(string)
    keep = array[:] #copy array to keep
    for i in range(len(array)-len(f)+1):
        if keep[i]== 1 or keep[i]== '1':
            #normal add
            a=''
            for i in range(len(array)):
                if i>=len(f):
                    a = a + str(int(keep[i])%2)
                else:
                    a = a + str((int(keep[i])+int(f[i]))%2)
            keep=a[:]
        f=np.insert(f,0,0)
    x=''
    for j in range(-1,-deg-1,-1):
        x=x+str(int(keep[j]))
    y ="["+x+"]"
    return y


def div(array1,array2,f,len_f,deg,all_ele):
    if array2=='[000]':
        return "error"
    else:
        for i in all_ele:
            if mul(array2,i,f,len_f,deg)==array1:
                return i
                break


print("INPUT: linear_equation_F256.txt")
with open("linear_equation_F256.txt") as file:
    lines = file.read().splitlines()

data=[]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j]=="=":
            data.append(lines[i][j+1:])
            break

n=int(data[0])
m=int(data[1])
print("n=" + str(n))
print("m=" + str(m))

#make all element in column and row
p=[]
for i in range(2**m):
    x=str(bin(i)[2:])
    if len(x)<m:
        for j in range(m-len(x)):
            x="0"+x
    x=x[::-1]
    x="["+x+"]"
    p.append(x)


#get value f
ele_f=data[2]

f=[] #make list of string ['1', '1', '0', '1']
len_f=0
for i in range(len(ele_f)):
    if ele_f[i] == '0' or ele_f[i] == '1':
        f.append(ele_f[i])
        len_f+=1 #count element in f

f_int=[] #make array [1 1 0 1]
for i in range(len(ele_f)):
    if ele_f[i] == '0' or ele_f[i] == '1':
        f_int.append(int(ele_f[i]))
f_int = np.asarray(f_int) #change list to array


#get value A and b
line_a=[]
line_b=[]
for k in range(5,5+n):
    line_a.append(lines[k][:])

for z in range(6+n,len(lines)):
    line_b.append(lines[z][:])

#get value A
a=[]
for i in range(n): #row
    ele_a=line_a[i]
    ele_a_in=[]
    j=0
    s=0
    while s != n: #n element in one row
        x=''
        for k in range(j,m+j+2):
            x=x+ele_a[k]
        ele_a_in.append(x)
        s+=1
        j=m+j+2
    a.append(ele_a_in)

A = np.array(a)
print("A=")
print_array(A)

#get value b
b=[]
for i in range(n): #row
    ele_b=line_b[i]
    ele_b_in=[]
    x=''
    for k in range(m+2):
        x=x+ele_b[k]
    ele_b_in.append(x)
    b.append(ele_b_in)

B = np.array(b)
print("b=")
print_array(B)

AB = np.append(A,B,axis=1)
lenAB = len(AB[0])

###

for i in range(n):   #column
    for j in range(i,n): #row
        if AB[j][i] == '[000]':
            if j == n-1:  #if it is the last one go to the next column
                break
            else:
                AB[[j,j+1]]=AB[[j+1,j]]  #if it is not the last one swap with the next row
        if AB[j][i] != '[100]':
            keep = AB[j][i]
            for k in range(i,lenAB):  #divide all element in row with first number(keep)
                AB[j][k]=div(AB[j][k],keep,f,len_f,m,p)


#get first element of all row become 1
#make the lower row become 0
    for h in range(i+1,n): #row
        if AB[h][i] != '[000]':
            for k in range(lenAB):  #all element in row
                AB[h][k]=add(AB[h][k],AB[i][k])


for i in range(n-1,-1,-1): #column
    for j in range(i):  #row
        deg = AB[j][i]
        for h in range(i,lenAB):
            keep = mul(AB[i][h],deg,f,len_f,m)
            AB[j][h]=add(AB[j][h],keep)

x=AB[:,n].reshape(n,1)

print("OUTPUT:")
print("x=")
print_array(x)
