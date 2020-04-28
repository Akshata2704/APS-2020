# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:27:41 2020

@author: AKSHATA
"""

def check(n):
    o=list(str(n))
    f=len(o)
    i=0
    j=f-1
    while(i<=j):
        if(o[i]!=o[j]):
            return 0
        i+=1
        j-=1
    return 1

n=int(input())
if(check(n)==0):
    print("NO")
else:
    print("YES")