# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:05:03 2020

@author: AKSHATA
"""

def leaders(A,N):
    arr=[]
    ida=[]
    arr.append(A[N-1])
    ida.append(N-1)
    i=N-2
    while(i>=0):
        j=i+1
        fl=0
        if(A[i]>=arr[(len(arr)-1)]):
            while(j<ida[len(ida)-1]):
                if(A[i]<A[j]):
                    fl=1
                    break
            
                j+=1
            if(fl==0):
                arr.append(A[i])
                ida.append(i)
        i-=1
        
    return reversed(arr)

for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    print(leaders(A,N))