# -*- coding: utf-8 -*-

x = input()
y = x.split()
a = int(y[0])
b = int(y[1])
total = 0
if a == 1:
    total = 4 * b
elif a == 2:
    total = 4.50 * b
elif a == 3:
    total = 5 * b
elif a == 4:
    total = 2 * b
elif a == 5:
    total = 1.50 * b
print('Total: R$ {:.2f}'.format(total))