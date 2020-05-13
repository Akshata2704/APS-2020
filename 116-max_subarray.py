# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:25:21 2020

@author: AKSHATA
"""

def maxLen(arr):
    n=len(arr)
    a=arr.count(1)
    b=n-a
    print(a,b)
    print(a+b)
    return 2*(min(a,b))

ar=list(map(int,input().split()))
print(maxLen(ar))