# -*- coding: utf-8 -*-
"""
Created on Sat May  9 01:22:53 2020

@author: AKSHATA
"""

def rotateArr(A,D,N):
    s=[0 for _ in range(N)]
    for i in range(N):
        ind=i-D;
        if(ind<0):
            ind=N+ind
        s[ind]=A[i]
    for i in range(len(s)):
        A[i]=s[i]
        
t=int(input())
for _ in range(t):
    N,D=map(int,input().split())
    A=list(map(int,input().split()))
    rotateArr(A,D,N)
    for i in range(N):
        print(A[i],end=" ")
    print()