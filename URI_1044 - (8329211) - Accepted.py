# -*- coding: utf-8 -*-

valor = input()
corta = valor.split()
a = int(corta[0])
b = int(corta[1])

if b % a == 0 or a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')