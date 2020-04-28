# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:39:36 2020

@author: AKSHATA
"""

def Sum(n):
    s=0
    while(n>0):
        s+=n%10
        n/=10
        n=int(n)
    return s
def getN(n):
    s=Sum(n)
    if(s%10==0):
        return n*10
    ex=int(10-(s%10))
    return int((n*10)+ex)

n=10
for i in range(1,n+1):
    print(getN(i))