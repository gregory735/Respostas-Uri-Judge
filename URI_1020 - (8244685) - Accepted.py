# -*- coding: utf-8 -*-

i = int(input(''))

a = i // 365
m = (i - (a * 365)) // 30
d = (i - (a * 365)) - (m *30)

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))