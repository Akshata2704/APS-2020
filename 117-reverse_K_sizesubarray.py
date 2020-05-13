# -*- coding: utf-8 -*-
"""
Created on Sat May  9 01:08:04 2020

@author: AKSHATA
"""

def reverseInGroups(A,N,K):
    a=[]
    i=0
    while(i+K<N):
        s=A[i:i+K]
        j=len(s)-1
        while(j>=0):
            a.append(s[j])
            j-=1
        i+=K
    if(i<N):
        s=A[i:N]
        j=len(s)-1
        while(j>=0):
            a.append(s[j])
            j-=1
    return a

t=int(input())
for _ in range(t):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A=reverseInGroups(A,N,K)
    for i in range(N):
        print(A[i],end=" ")
    print()
    