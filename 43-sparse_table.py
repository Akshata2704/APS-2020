# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:37:18 2020

@author: AKSHATA
"""
import math
inputa=[]

def pre(n):
    global inputa
    sparse=[[0 for _ in range(math.floor((math.log2(n))+1))] for _ in range(n+1)]

    for i in range(n):
        sparse[i][0]=i;
    j=1
    while((1<<j)<=n):
        i=0
        while((i+(1<<j)-1)<n):
            if(inputa[sparse[i][j-1]]<inputa[sparse[i+(1<<(j-1))][j-1]]):
                sparse[i][j]=sparse[i][j-1]
            else:
                sparse[i][j]=sparse[i+(1<<(j-1))][j-1]
            i+=1
        j+=1
    return sparse

def req(sparse,lo,h):
    global inputa
    l=h-lo+1
    k=math.floor(math.log2(l))
    return min(inputa[sparse[lo][k]],inputa[sparse[lo+l-(1<<k)][k]])
n=6
inputa=list(map(int,input().split()))
sparse=pre(n)
print(req(sparse,1,5))