# -*- coding: utf-8 -*-

v1 = 1
vc = 0
v2 = 60
for i in range (0,12    ):
    if vc == 0:
        print('I=1 J=60')
    v1 += 3
    v2 -=5
    vc+=1
    print('I={} J={}'.format(v1,v2))