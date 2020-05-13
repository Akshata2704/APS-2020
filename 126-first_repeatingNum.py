# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:15:08 2020

@author: AKSHATA
"""
def firstRepeated(arr, n):
    d={}
    ida=[]
    for i in range(n):
        if(arr[i] not in d):
            d[arr[i]]=i+1
        else:
            ida.append(d[arr[i]])
    if(ida):
        ida.sort()
        return ida[0]
    return -1

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(firstRepeated(arr,n))