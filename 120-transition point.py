# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:33:59 2020

@author: AKSHATA
"""

def transitionPoint(arr, n):
    for i in range(n):
        if(arr[i]==1):
            return i;
    return -1

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(transitionPoint(arr,n))
    