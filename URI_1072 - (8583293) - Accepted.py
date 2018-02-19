# -*- coding: utf-8 -*-
t=int(input())
a=[]
n=0
out=0
for i in range(0,t):
    k=int(input())
    a.append(k)
for i in range(0,t):
    if((a[i]>=10) and (a[i]<=20) ):
        n+=1
    else:
        out+=1
print("{} in".format(n))
print("{} out".format(out))