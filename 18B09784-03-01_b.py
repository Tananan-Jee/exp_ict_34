# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784-03-01_b.py
#実行方法：ターミナル上で python3 18B09784-03-01_b.py を実行


print("INPUT: vec.txt")
with open("vec.txt") as file:
    lines = file.read().splitlines()

#read data in vec.txt and keep in data
data=[]
for i in range(len(lines)):
    print(lines[i])
    for j in range(len(lines[i])):
        if lines[i][j]=="=":
            data.append(lines[i][j+1:])
            break

#c1=data[0]
#c2=data[1]

count = 0
for i in range(int(data[0])):
    if data[1][i]!=data[2][i]:
        count+=1

print("OUTPUT:")
print("d=" + str(count))
