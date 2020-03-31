# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#***コンパイル方法：python3 18B09784-04-06_c.py
#****実行方法：ターミナル上で python3 18B09784-04-06_c.py を実行

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
    if array2=='[00000000]':
        return "error"
    else:
        for i in all_ele:
            if mul(array2,i,f,len_f,deg)==array1:
                return i
                break


print("INPUT: RS256_decode_example.txt")
with open("RS256_decode_example.txt") as file:
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

d_min=n-k+1
t=int(math.floor((d_min-1)/2))


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


#get value r
get_r=[]
for z in range(5,6):
    i = 0
    while i != n*(m+2):
        get_r.append(lines[z][i])
        i+=1

r=[]
ele_r=get_r[:]
ele_r_in=[]
j=0
s=0
while s != n: #n element in one row
    x=''
    for i in range(j,m+j+2):
        x=x+ele_r[i]
    ele_r_in.append(x)
    s+=1
    j=m+j+2
r.append(ele_r_in)

R = np.array(r)


#make a_0
A_0=[]
for j in range(n):
    a_0=[]
    for i in range(n-t):
        if i==0:
            keep = '[10000000]'
        else:
            keep = mul(keep,all_alpha[j],f,len_f,m)
        a_0.append(keep)
    A_0.append(a_0)

#print_array(A_0)

A_1=[]
for j in range(n): #row
    a_1=[]
    ans='[00000000]'
    for i in range(t+1):
        if i==0:
            keep = '[10000000]'
        else:
            keep = mul(keep,all_alpha[j],f,len_f,m)
        keep_r = mul(keep,R[0][j],f,len_f,m)
        a_1.append(keep_r)
    A_1.append(a_1)
#print_array(A_1)

A = np.append(A_0,A_1,axis=1)
print_array(A)

lenA = len(A[0])
all_alpha.append('[00000000]')
###

for i in range(n):   #column
    for j in range(i,n): #row
        if A[j][i] == '[00000000]':
            if j == n-1:  #if it is the last one go to the next column
                break
            else:
                A[[j,j+1]]=A[[j+1,j]]  #if it is not the last one swap with the next row
        if A[j][i] != '[10000000]':
            keep = A[j][i]
            for k in range(i,lenA):  #divide all element in row with first number(keep)
                A[j][k]=div(A[j][k],keep,f,len_f,m,all_alpha)

    print_array(A)

#get first element of all row become 1
#make the lower row become 0
    for h in range(i+1,n): #row
        if A[h][i] != '[00000000]':
            for s in range(lenA):  #all element in row
                A[h][s]=add(A[h][s],A[i][s])


for i in range(n-1,-1,-1): #column
    for j in range(i):  #row
        deg = A[j][i]
        for h in range(i,lenA):
            keep = mul(A[i][h],deg,f,len_f,m)
            A[j][h]=add(A[j][h],keep)

x=A[:,n].reshape(n,1)

print("OUTPUT:")
print("x=")
print_array(x)

#c=[]
#for j in range(n): #length c
#    ans='[00000000]'
#    for i in range(k):
#        if i==0:
#            keep = '[10000000]'
#        else:
#            keep = mul(keep,all_alpha[j],f,len_f,m)
#        keep_u = mul(keep,U[0][i],f,len_f,m)
#        ans = add(keep_u,ans)
#    c.append(ans)
#
#C = np.array([c])
#print_array(C)

#G=[]
#for q in range(k): #row
#    keep =[]
#    for i in p:
#        print(p)
#        power_g = power(i,q,f,len_f,m)
#        print(power_g)
#        keep.append(power_g)
#        print(keep)
#    keep_g=np.array(keep)
#    G = np.append(G,keep_g,axis=0)

#print(G[0])

###
