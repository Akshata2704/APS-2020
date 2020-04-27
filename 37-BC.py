# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:06:44 2020

@author: AKSHATA
"""

n=5
k=5
c=[[0 for _ in range(k)]for _ in range(n)]
for i in range(0,n):
    for j in range(0,min(i,k)+1):
        if(j==0 or j==n):
            c[i][j]=1;
        else:
            c[i][j]=c[i-1][j-1]+c[i-1][j];
print(c[n-1][k-1])