# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 01:05:34 2020

@author: AKSHATA
"""

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a,b=map(int,input().split())
print((a*b)/gcd(a,b))