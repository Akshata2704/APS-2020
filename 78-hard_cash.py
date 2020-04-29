# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:11:12 2020

@author: AKSHATA
"""
t=int(input());
final=[]
rem=[0]
if(1<=t<=1000):
    for _ in range(t):
        sum=0;
        nk=input().split()
        n=int(nk[0]);
        k=int(nk[1]);
        coin=list(map(int,input().split()))
        rem.clear()
        for i in range(n):
            sum=sum+(coin[i]%k);
        final.append(sum%k);
        
    for i in range(t):
        print(final[i]);  
    