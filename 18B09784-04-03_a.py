# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-04-03_a.py
#実行方法：ターミナル上で python3 18B09784-04-03_a.py を実行

import math
import numpy as np

def print_array(array):
    print("[", end='')
    for i in range(len(array)):
        print(int(array[i]), end='')
    print("]")

def plus(array1,array2):
    array=[]
    length=min(len(array1),len(array2))
    for i in range(length):
        array_ele=(int(array1[i])+int(array2[i]))%2
        array.append(array_ele)
    if len(array1)>len(array2):
        for j in range(length,len(array1)):
            array.append(int(array1[j]))
    else:
        for j in range(length,len(array2)):
            array.append(int(array2[j]))
    return array

def mul(array1,array2,deg):
    array=np.zeros(deg+1)
    for i in range(len(array1)):
        for j in range(len(array2)):
            array[i+j]=(array[i+j]+(int(array2[j])*int(array1[i])))%2
    return array


def div(array1,array2,diff):
    ans=np.zeros(diff+1)
    array1=array1[::-1]
    array2=array2[::-1]
    keep = array1[:]
    for i in range(diff+1):
        if keep[i]== 1 or keep[i]== '1':
            ans[i]=1                    #'1'01101101
            keep=plus(keep,array2)      # 101101101 + 11111 = 010011101 , ans = 1
        else:
            ans[i]=0
        array2.insert(0,0) #11111 -> '0'11111
                           # ans = 11101 remainder = 000000110
    ans = ans[::-1] #11101 => 10111

    while keep[0]==0: #remainder = 000000110 -> 110
        del keep[0]
    rem = keep[::-1] #110 ->011

    print("quotient ", end='')
    print_array(ans)
    print("remainder ", end='')
    print_array(rem)


print("INPUT:")
n=int(input("n="))
m=int(input("m="))
ele_f=str(input("f="))
ele_g=str(input("g="))

f=[]
for i in range(len(ele_f)):
    if ele_f[i] == '0' or ele_f[i] == '1':
        f.append(ele_f[i])

g=[]
for i in range(len(ele_g)):
    if ele_g[i] == '0' or ele_g[i] == '1':
        g.append(ele_g[i])


print("OUTPUT:")
print("f+g=", end='')
print_array(plus(f,g))
print("f-g=", end='')
print_array(plus(f,g))
print("f*g=", end='')
print_array(mul(f,g,n+m))
print("f/g=", end='')
div(f,g,n-m)
