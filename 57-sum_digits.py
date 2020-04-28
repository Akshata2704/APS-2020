# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:30:47 2020

@author: AKSHATA
"""

def sumd(n):
    s=0
    while(n!=0):
        j=n%10
        s+=j
        n/=10
        n=int(n)
    return s

n=int(input())
print(sumd(n))