# -*- coding: utf-8 -*-

X = input()
Y = X.split()

A = int(Y[0])
B = int(Y[1])
C = int(Y[2])
D = int(Y[3])

if B > C and D > A and C + D > A + B and C > 0 and B > 0 and A % 2 == 0:

    print('Valores aceitos')

else:
    print('Valores nao aceitos')