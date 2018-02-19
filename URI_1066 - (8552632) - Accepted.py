# -*- coding: utf-8 -*-

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

n = 0
c1 = 0
c2 = 0
c3 = 0
if n1 % 2 == 0:
    n = n + 1
if n2 % 2 == 0:
    n = n + 1
if n3 % 2 == 0:
    n = n + 1
if n4 % 2 == 0:
    n = n + 1
if n5 % 2 == 0:
    n = n + 1
#impar
if n1 % 2 != 0:
    c1 = c1 + 1
if n2 % 2 != 0:
    c1 = c1 + 1
if n3 % 2 != 0:
    c1 = c1 + 1
if n4 % 2 != 0:
    c1 = c1 + 1
if n5 % 2 != 0:
    c1 = c1 + 1
#positivo
if n1 > 0:
    c2 = c2 + 1
if n2 > 0:
    c2 = c2 + 1
if n3 > 0:
    c2 = c2 + 1
if n4 > 0:
    c2 = c2 + 1
if n5 > 0:
    c2 = c2 + 1
#negativo
if n1 < 0:
    c3 = c3 + 1
if n2 < 0:
    c3 = c3 + 1
if n3 < 0:
    c3 = c3 + 1
if n4 < 0:
    c3 = c3 + 1
if n5 < 0:
    c3 = c3 + 1

print('{} valor(es) par(es)'.format(n))
print('{} valor(es) impar(es)'.format(c1))
print('{} valor(es) positivo(s)'.format(c2))
print('{} valor(es) negativo(s)'.format(c3))