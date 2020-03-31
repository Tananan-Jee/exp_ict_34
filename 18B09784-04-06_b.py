# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-04-06_b.py
#実行方法：ターミナル上で python3 18B09784-04-06_b.py を実行

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


print("INPUT: RS256_encode_problem.txt")
with open("RS256_encode_problem.txt") as file:
    lines = file.read().splitlines()


data=[]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j]=="=":
            data.append(lines[i][j+1:])
            break

n=int(data[1])
k=int(data[2])
print("n=" + str(n))
print("k=" + str(k))

#get value f
ele_f=data[0]

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


m=len_f-1 #length of each alpha


#make array of all alpha
all_alpha=[]
alpha='[01000000]'
for i in range(n):
    if i==0:
        x='[10000000]'
    else:
        x=mul(x,alpha,f,len_f,m)
    all_alpha.append(x)


#get value u
a=[]
for z in range(5,6):
    i = 0
    while i != k*(m+2):
        a.append(lines[z][i])
        i+=1

u=[]
ele_u=a[:]
ele_u_in=[]
j=0
s=0
while s != k: #k element in one row
    x=''
    for i in range(j,m+j+2):
        x=x+ele_u[i]
    ele_u_in.append(x)
    s+=1
    j=m+j+2
u.append(ele_u_in)

U = np.array(u)
print("u=")
print_array(U)

#find c
c=[]
for j in range(4): #length c
    ans='[00000000]'
    for i in range(k):
        if i==0:
            keep = '[10000000]'
        else:
            keep = mul(keep,all_alpha[j],f,len_f,m)
        keep_u = mul(keep,U[0][i],f,len_f,m)
        ans = add(keep_u,ans)
    c.append(ans)

C = np.array([c])

print("OUTPUT:")
print("C=")
print_array(C)
