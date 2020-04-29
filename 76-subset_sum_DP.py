# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:36:54 2020

@author: AKSHATA
"""
def fnd(ss,S):
    n=len(ss)+1
    a=[[0 for _ in range(S+1)] for _ in range(len(ss)+1)]
    for i in range(0,n):
        a[i][0]=1
    for i in range(1,n):
        for j in range(1,S+1):
            if(a[i-1][j]==1):
                a[i][j]=1
            elif(ss[i-1]>j):
                a[i][j]=0
            else:
                a[i][j]=a[i-1][j-ss[i-1]]
    return a[n-1][S]
   
ss=list(map(int,input().split()))
S=int(input())
if(fnd(ss,S)):
    print("YES")
else:
    print("NO")
