# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:11:54 2020

@author: AKSHATA
"""

def bc(n,k):
    if(n==k):
        return 1;
    return bc(n-1,k-1)+bc(n-1,k)

n=5
k=5
print(bc(n,k))
