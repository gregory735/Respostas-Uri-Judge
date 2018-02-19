# -*- coding: utf-8 -*-

import math
A = input()
B = input()

C = A.split()
D = B.split()

Y1 = float(C[0])
X1 = float(C[1])

Y2 = float(D[0])
X2 = float(D[1])

R = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)

print('{:.4f}'.format(R))