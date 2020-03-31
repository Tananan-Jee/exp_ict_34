# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-04-04_a.py
#実行方法：ターミナル上で python3 18B09784-04-04_a.py を実行

import math
import numpy as np

def add(array1,array2):
    array=''
    for i in range(1,len(array1)-1):
        if array1[i] != "[" or array1[i] != "]":
            array = array + str((int(array1[i])+int(array2[i]))%2)
    print("[" + array + "] ", end="")


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
        return "-----"
    else:
        for i in all_ele:
            if mul(array2,i,f,len_f,deg)==array1:
                return i
                break

#make head of the table
def head(num):
    print("      | ", end = '')
    for i in num:
        print(str(i) + " ", end = '')
    print("")
    print("------+-", end = '')
    for i in range(len(num)):
        print("------", end = '')
    print("")



print("INPUT:")
m=int(input("m="))

#make main column and row
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
ele_f=str(input("f(x)="))

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


print("OUTPUT:")

print("ADD")
head(p)
for i in p:
    print(str(i) + " | ", end = '')
    for j in p:
        add(i,j)
    print("")

print("MUL")
head(p)
for i in p:
    print(str(i) + " | ", end = '')
    for j in p:
        print(mul(i,j,f_int,len_f,m)+" ", end = '')
    print("")

print("SUB")
head(p)
for i in p:
    print(str(i) + " | ", end = '')
    for j in p:
        add(i,j)
    print("")

print("DIV")
head(p)
for i in p:
    print(str(i) + " | ", end = '')
    for j in p:
        print(div(i,j,f_int,len_f,m,p) + " ", end = '')
    print("")
