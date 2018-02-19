# -*- coding: utf-8 -*-

N = int(input(''))

c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0
D = N
if 0 < D < 1000000:
    while D >= 100:
        c100 += 1
        D = D - 100
    while D >= 50:
        c50 += 1
        D = D - 50
    while D >= 20:
        c20 += 1
        D = D - 20
    while D >= 10:
        c10 += 1
        D = D - 10
    while D >= 5:
        c5 += 1
        D = D - 5
    while D >= 2:
        c2 += 1
        D = D - 2
    while D >= 1:
        c1 += 1
        D = D - 1

print('{}'.format(N))
print('{} nota(s) de R$ 100,00'.format(c100))
print('{} nota(s) de R$ 50,00'.format(c50))
print('{} nota(s) de R$ 20,00'.format(c20))
print('{} nota(s) de R$ 10,00'.format(c10))
print('{} nota(s) de R$ 5,00'.format(c5))
print('{} nota(s) de R$ 2,00'.format(c2))
print('{} nota(s) de R$ 1,00'.format(c1))