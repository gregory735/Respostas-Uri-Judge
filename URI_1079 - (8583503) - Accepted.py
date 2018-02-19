# -*- coding: utf-8 -*-

n = int(input())
for i in range(1,n + 1):
    n =input()
    x = n.split()
    n1 = float(x[0])
    n2 = float(x[1])
    n3 = float(x[2])
    r = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
    print("{:.1f}".format(r))