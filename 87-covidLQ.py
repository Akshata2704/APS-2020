# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:25:08 2020

@author: AKSHATA
"""

T=int(input())
for _ in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    fl=1
    while(i<n):
        if(a[i]==1):
            N=i+5
            j=i+1
            s=0
            while(j<=N and j<n):
                s|=a[j]
                j+=1
            if(s==1):
                i=len(a)
                fl=0
                print("NO")
            else:
                i=i+6
        else:
            i+=1
    if(fl==1):
        print("YES")
        
        