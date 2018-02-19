# -*- coding: utf-8 -*-
n = int(input())
cont = 0
for i in range(0,10000,1):
    r = i % n
    if r == 2:
     print(i)