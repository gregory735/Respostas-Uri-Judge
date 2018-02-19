# -*- coding: utf-8 -*-

#entrada
notas = input()
#processamento
x = notas.split()
n1 = float(x[0])
n2 = float(x[1])
n3 = float(x[2])
n4 = float(x[3])
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
#saida
if media >= 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
elif media >= 5 and media < 7:
    exame = float(input(''))
    if exame < 5:
        exame = exame - 0.001
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    print('Nota do exame: {:.1f}'.format(exame))
    mediaf = (media + exame)/2
    if mediaf >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(mediaf))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(mediaf))