# -*- coding: utf-8 -*-

valor = input()
z = valor.split()
x = float(z[0])
y = float(z[1])
if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x != 0 and y == 0:
    print('Eixo X')
else:
    print('Origem')