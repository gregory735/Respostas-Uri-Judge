# -*- coding: utf-8 -*-
valor1 = input()
valor2 = input()
valor3 = input()

if valor1 == 'vertebrado':
    if valor2 == 'ave':
        if valor3 == 'carnivoro':
            print('aguia')
        if valor3 == 'onivoro':
            print('pomba')
    if valor2 == 'mamifero':
        if valor3 == 'onivoro':
            print('homem')
        if valor3 == 'herbivoro':
            print('vaca')

if valor1 == 'invertebrado':
    if valor2 == 'inseto':
        if valor3 == 'hematofago':
            print('pulga')
        if valor3 == 'herbivoro':
            print('lagarta')
    if valor2 == 'anelideo':
        if valor3 == 'hematofago':
            print('sanguessuga')
        if valor3 == 'onivoro':
            print('minhoca')