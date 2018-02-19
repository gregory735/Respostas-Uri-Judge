# -*- coding: utf-8 -*-

N = input()

K = N.split()
A = float(K[0])
B = float(K[1])
C = float(K[2])


D = A * C / 2
E = 3.14159 * C ** 2
F = ((A + B) / 2) * C
G = B ** 2
H = A * B

print('TRIANGULO: {:.3F}\nCIRCULO: {:.3F}\nTRAPEZIO: {:.3F}\nQUADRADO: {:.3F}\nRETANGULO: {:.3F}'.format(D,E,F,G,H))