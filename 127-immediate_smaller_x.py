# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:41:21 2020

@author: AKSHATA
"""

import sys
def immediateSmaller(arr,n,x):
    minm=sys.maxsize
    f=-1
    for i in range(n):
        if(arr[i]<x):
            if(x-arr[i]<minm):
                minm=x-arr[i]
                f=arr[i]
                
    if(minm!=sys.maxsize):
        return f
    return -1


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    x=int(input())
    print(immediateSmaller(arr,n,x))