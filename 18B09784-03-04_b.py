# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-03-04_b.py
#実行方法：ターミナル上で python3 18B09784-03-04_b.py を実行

import math
import numpy as np

def print_array(array):
    for i in range(len(array)):
        print(''.join(map(str,array[i])))

def plus(array1,array2):
    array=[]
    for i in range(len(array1)):
        array_ele=(int(array1[i])+int(array2[i]))%2
        array.append(array_ele)
    return array

def mul_array(array1,array2):
    array=[]
    array_row=[]
    row_num=len(array1)
    col_num=len(array2[0])
    mid=len(array2)
    for i in range(row_num):
        for j in range(col_num):
            get=0
            for s in range(mid):
                keep=int(array1[i][s])*int(array2[s][j])
                get=(get+keep)%2
            array_row.append(str(get))
        array.append(array_row)
    return array

#read file linearcode.txt
print("INPUT: linearcode.txt")
with open("linearcode.txt") as file:
    lines = file.read().splitlines()

#keep first 2 line in data
data=[]
for i in range(2):
    for j in range(len(lines[i])):
        if lines[i][j]=="=":
            data.append(lines[i][j+1:])
            break

n=int(data[0])
k=int(data[1])


ele=[]
for i in range(3,len(lines)):
    ele.append(lines[i][:])

g=[]
for i in range(k):
    ele_g=ele[i]
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
u=np.array(u_ele)

#make 情報ベクトル c=uG
c=[]
for i in range(len(u)):
    c.append(mul_array(u[i],G))

#find minimum distance by ハミング重み
d_min=0
for i in range(len(c)): #for all c
    count=0
    for j in range(n):
        if c[i][0][j]!='0':
            count+=1
        if d_min!=0:
            if d_min<=count: #if we found that it is going to have more distance than stored d_min go out from loop and check the next one
                break
    d_min=count


#find G'
for i in range(0,k): #check each row
    G_keep = []
    g_keep = []
    keep_up = []
    keep_down = []
    #make array G
    if i!=0:
        for j in range(0,i):
            g_keep.append(G[j])
            G_keep=np.array(g_keep)
    for w in range(i,k): #check the lower row
        if G[w][i]=='1': #if front number is '1' keep in keep_up
            keep_up.append(w)
        else: #if front number is '0' keep in keep_down
            keep_down.append(w)
    #push the row in keep_up go up and in keep_down go down
    for x in keep_up:
        g_keep.append(G[x])
        G_keep=np.array(g_keep)
    for l in keep_down:
        g_keep.append(G[l])
        G_keep=np.array(g_keep)
    #plus the lower row that front number is '1' with the row i -> '1' become '0'
    if len(keep_up)>1:
        for m in range(1,len(keep_up)):
            G_keep[m+i]=plus(G_keep[i],G_keep[m+i])
    G=G_keep[:]
#until here we get G matix with upper triangular matrix

#make left side to be identity matrix
for i in range(k-1,-1,-1):
    keep=[]
    for w in range(0,i):
        if G[w][i]=='1':
            keep.append(w)
    if len(keep)>=1:
        for m in keep:
            if m!=i:
                G[m]=plus(G[i],G[m])



P=G[:,k:].reshape(k,n-k) #right side of G = P
P_tran=np.transpose(P) #P transpose
iden_h=np.eye(n-k) #n-k identity matrix
iden_h = iden_h.astype(np.int) #change element to be integer

#make H = [P^T iden_h]
H=np.append(P_tran,iden_h,axis=1)

H = H.astype(np.int)
G = G.astype(np.int)
G_ori = G_ori.astype(np.int)
tran_H=np.transpose(H)
dot_g=(G.dot(tran_H))%2
dot_gori=(G_ori.dot(tran_H))%2


print("OUTPUT:")
print("M=" + str(2**k))
print("R=" + str(k/n))
print("d_min=" + str(d_min))
print("G'=")
print_array(G)
print("H'=")
print_array(H)
print("G(H')^T=")
print_array(dot_gori)
print("G'(H')^T=")
print_array(dot_g)
