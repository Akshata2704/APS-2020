# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:24:43 2020

@author: AKSHATA
"""

a=list(map(int,input().split()))
LIS=[1]*len(a)
for i in range(1,len(a)):
    for j in range(0,i):
        if(a[i]>a[j] and LIS[j]+1>LIS[i]):
            LIS[i]=LIS[j]+1
print(LIS[len(a)-1])