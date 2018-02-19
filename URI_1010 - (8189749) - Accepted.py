# -*- coding: utf-8 -*-

A = input()
B = A.split()
C = int(B[0])
D = int(B[1])
E = float(B[2])

F = input()
G = F.split()
H = int(G[0])
I = int(G[1])
J = float(G[2])

K = D * E + I * J

print('VALOR A PAGAR: R$ {:.2f}'.format(K))