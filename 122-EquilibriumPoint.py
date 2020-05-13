# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:54:41 2020

@author: AKSHATA
"""

def equilibriumPoint(A, N):
    if(N==1):
        return 1
    i=0
    mid=1
    sb=A[i]
    sa=sum(A[mid+1:N])
    while(sa>=A[N-1]):
        if(sb==sa):
            return mid+1
        else:
            sb+=A[mid]
            sa-=A[mid+1]
            mid+=1
    return -1

for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    print(equilibriumPoint(A,N))