# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:19:18 2020

@author: AKSHATA
"""

n=int(input())
k=list(map(int,input().split()))
a=[0]*(n+1)
a[0]=1
for i in range(0,len(k)):
    for j in range(k[i],n+1):
        a[j]=a[j]+a[j-k[i]]
print(a[n])
