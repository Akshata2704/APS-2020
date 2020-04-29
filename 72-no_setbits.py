# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:13:25 2020

@author: AKSHATA
"""

def nu(n):
    c=0
    while(n!=0):
        n=n&(n-1)
        c+=1
    return c

n=int(input())
print(nu(n))