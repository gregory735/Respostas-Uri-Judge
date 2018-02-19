# -*- coding: utf-8 -*-

N = int(input(''))

H = N // 3600
M = (N % 3600) // 60
S = N % 60

print('{}:{}:{}'.format(H,M,S))