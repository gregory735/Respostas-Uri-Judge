# -*- coding: utf-8 -*-

s = float(input())

if s >= 0 and s <= 400:
    aumento = s * 15 / 100
    salario = aumento + s
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(aumento))
    print('Em percentual: 15 %')

elif s >= 400.01 and s <= 800:
    aumento = s * 12 / 100
    salario = aumento + s
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(aumento))
    print('Em percentual: 12 %')

elif s >= 800.01 and s <= 1200:
    aumento = s * 10 / 100
    salario = aumento + s
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(aumento))
    print('Em percentual: 10 %')

elif s >= 1200.01 and s <= 2000:
    aumento = s * 7 / 100
    salario = aumento + s
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(aumento))
    print('Em percentual: 7 %')

elif s > 2000:
    aumento = s * 4 / 100
    salario = aumento + s
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(aumento))
    print('Em percentual: 4 %')