# -*- coding: utf-8 -*-

v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
n = 0
if v1 % 2 == 0:
    n = n + 1
if v2 % 2 == 0:
    n = n + 1
if v3 % 2 == 0:
    n = n + 1
if v4 % 2 == 0:
    n = n + 1
if v5 % 2 == 0:
    n = n + 1

print('{} valores pares'.format(n))