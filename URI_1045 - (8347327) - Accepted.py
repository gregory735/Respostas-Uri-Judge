# -*- coding: utf-8 -*-
val=input()
corta = val.split()
a=float(corta[0])
b=float(corta[1])
c=float(corta[2])

lados = a+b+c
A = max(a, b, c)
B = min(a, b, c)
C = lados - (A + B)
C = round(C,10)

if A >= (B + C):
    print ('NAO FORMA TRIANGULO')
else:
    if (A ** 2)==(B ** 2) + (C ** 2):
        print ('TRIANGULO RETANGULO')
        
    if (A ** 2) > (B ** 2) + (C ** 2):
        print ('TRIANGULO OBTUSANGULO')
        
    if (A ** 2) < ( B ** 2 + C ** 2):    
        print ('TRIANGULO ACUTANGULO')
        
    if A == B and A == C and B == C:
        print ('TRIANGULO EQUILATERO')
        
    elif (A == B) and (B != C) or (B == C) and (C !=A ) or ( A == C) and (C != B):
        print ('TRIANGULO ISOSCELES')