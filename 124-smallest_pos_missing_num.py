# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:58:00 2020

@author: AKSHATA
"""

def missingNumber(arr,n):
    a=[]
    cnt=0
    for i in range(n):
        if(arr[i]>0):
            a.append(arr[i])
            cnt+=1
            
    
        
            
    at=[0 for i in range(cnt+1)]
    at[0]=-1
    for j in range(cnt):
        if(a[j]<=cnt):
            at[a[j]]=-1
    for i in range(cnt+1):
        if(at[i]==0):
            return i
    return cnt+1

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(missingNumber(arr,n))