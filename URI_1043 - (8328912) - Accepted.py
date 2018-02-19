# -*- coding: utf-8 -*-

valor = input()
corta = valor.split()
a = float(corta[0])
b = float(corta[1])
c = float(corta[2])

if a < b + c and b < a + c and c < a + b:
    perimetro = a + b + c
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area = ((a + b) * c) / 2
    print('Area = {:.1f}'.format(area))