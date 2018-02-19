# -*- coding: utf-8 -*-

A = input()
B = A.split()
C = int(B[0])
D = int(B[1])
E = int(B[2])

M = (C + D + abs(C - D)) / 2
R = (M + E + abs(M - E)) / 2

print('{} eh o maior'.format(int(R)))