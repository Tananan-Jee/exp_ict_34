# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-03-01_a.py
#実行方法：ターミナル上で python3 18B09784-03-01_a.py を実行

print("INPUT:")
len=int(input("n="))
c_0=str(input("c0="))
c_1=str(input("c1="))


count = 0
for i in range(len):
    if c_0[i]!=c_1[i]:
        count+=1

print("OUTPUT:")
print("d=" + str(count))
