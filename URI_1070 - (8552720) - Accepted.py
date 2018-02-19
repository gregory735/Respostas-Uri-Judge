# -*- coding: utf-8 -*-

n1 = int(input())
c1 = n1
c2 = n1
for i in range(1,7,1):
  if c1 % 2 == 0:
    c1 += 1
  elif c1 % 2 !=0:
      c1 += 2
  print(c1)