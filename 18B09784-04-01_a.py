# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-04-01_a.py
#実行方法：ターミナル上で python3 18B09784-04-01_a.py を実行

import math
import numpy as np


def add(ele1,ele2,mod):
    return (ele1+ele2)%mod

def sub(ele1,ele2,mod):
    return (ele1-ele2)%mod

def mul(ele1,ele2,mod):
    return (ele1*ele2)%mod

def div(ele1,ele2,mod):
    if ele2 == 0:
        return "-"
    else:
        for i in range(mod):
            if (i*ele2)%mod == ele1:
                return i
                break

#make head of the table
def head(num):
    print("  | ", end = '')
    for i in range(num):
        print(str(i) + " ", end = '')
    print("")
    print("--+-", end = '')
    for i in range(num):
        print("--", end = '')
    print("")


print("INPUT:")
p=int(input("p="))

print("OUTPUT:")

print("ADD")
head(p)
for i in range(p):
    print(str(i) + " | ", end = '')
    for j in range(p):
        print(str(add(i,j,p)) + " ", end = '')
    print("")

print("MUL")
head(p)
for i in range(p):
    print(str(i) + " | ", end = '')
    for j in range(p):
        print(str(mul(i,j,p)) + " ", end = '')
    print("")

print("SUB")
head(p)
for i in range(p):
    print(str(i) + " | ", end = '')
    for j in range(p):
        print(str(sub(i,j,p)) + " ", end = '')
    print("")

print("DIV")
head(p)
for i in range(p):
    print(str(i) + " | ", end = '')
    for j in range(p):
        print(str(div(i,j,p)) + " ", end = '')
    print("")
