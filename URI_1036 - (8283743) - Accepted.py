# -*- coding: utf-8 -*-

from math import sqrt
X = input()
Y = X.split()
A = float(Y[0])
B = float(Y[1])
C = float(Y[2])
if A != 0:
    delta = (B ** 2) - ((4 * A) * C)
    if delta > 0:
        x1 = (- B + sqrt(delta)) / (2 * A)
        x2 = (- B - sqrt(delta)) / (2 * A)
        print('R1 = {:.5f}'.format(x1))
        print('R2 = {:.5f}'.format(x2))
    elif delta < 0:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')