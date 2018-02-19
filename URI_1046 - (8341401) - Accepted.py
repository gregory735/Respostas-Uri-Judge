# -*- coding: utf-8 -*-

valor = input()
corta = valor.split()
x = int(corta[0])
y = int(corta[1])
if x >= y:
    tempo = ((24 - x) + y)
    print('O JOGO DUROU {} HORA(S)'.format(tempo))
else:
    tempo = y - x
    print('O JOGO DUROU {} HORA(S)'.format(tempo))