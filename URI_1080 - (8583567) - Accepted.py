# -*- coding: utf-8 -*-
mx = 1
pos = 1
for i in range(0,100):
    n = int(input())
    if n > mx:
        mx = n
        pos = i + 1
print(mx)
print(pos)