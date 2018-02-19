# -*- coding: utf-8 -*-

N = float(input())
c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0

m1 = 0
m050 = 0
m025 = 0
m010 = 0
m005 = 0
m0001 = 0

if N >= 0 and N <= 1000000.00:
    while N >= 100:
        c100 += 1
        N = N - 100
    while N >= 50:
        c50 += 1
        N = N - 50
    while N >= 20:
        c20 += 1
        N = N - 20
    while N >= 10:
        c10 += 1
        N = N - 10
    while N >= 5:
        c5 += 1
        N = N - 5
    while N >= 2:
        c2 += 1
        N = N - 2

    while N >= 1:
        m1 += 1
        N = N - 1
    while N >= 0.50:
        m050 += 1
        N = N - 0.50
    while N >= 0.25:
        m025 += 1
        N = N - 0.25
    while N >= 0.10:
        m010 += 1
        N = N - 0.10
    while N >= 0.05:
        m005 += 1
        N = N - 0.05
    while N >= 0.01:
        m0001 += 1
        N = N - 0.01
    while N >= 0.001:
        m0001 += 1
        N = N - 0.01 + 0.001
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(c100))
print('{} nota(s) de R$ 50.00'.format(c50))
print('{} nota(s) de R$ 20.00'.format(c20))
print('{} nota(s) de R$ 10.00'.format(c10))
print('{} nota(s) de R$ 5.00'.format(c5))
print('{} nota(s) de R$ 2.00'.format(c2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(m1))
print('{} moeda(s) de R$ 0.50'.format(m050))
print('{} moeda(s) de R$ 0.25'.format(m025))
print('{} moeda(s) de R$ 0.10'.format(m010))
print('{} moeda(s) de R$ 0.05'.format(m005))
print('{} moeda(s) de R$ 0.01'.format(m0001))