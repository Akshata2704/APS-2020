# -*- coding: utf-8 -*-
"""
Created on Mon May 11 01:36:25 2020

@author: AKSHATA
"""

def convertToWave(A,N):
    i=0
    while(i+1<N):
        A[i],A[i+1]=A[i+1],A[i]
        i+=2
for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    convertToWave(A,N)
    for i in range(N):
        print(A[i],end=" ")
    print()