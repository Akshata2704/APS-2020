# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:15 2020

@author: AKSHATA
"""
def bc(n,k):
    for i in range(1,n):
        j=min(i,k)
        while(j>0):
            c[j]+=c[j-1]
            j-=1
    return c[k-1]
n=4
k=2
c=[0 for _ in range(n+1)]
c[0]=1;
print(bc(n,k))
