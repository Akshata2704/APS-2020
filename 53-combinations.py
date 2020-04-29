# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:31:54 2020

@author: AKSHATA
"""

def fact(j):
    s=1
    while(j!=1):
        s=s*j;
        j-=1
    return s
        
        
def comb(n,r):
    return fact(n)/(fact(n-r)*fact(r))
n,r=map(int,input().split())
if(n<r):
    print("Invalid input")
else:
    print(comb(n,r))