# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:36:03 2020

@author: AKSHATA
"""

def simple_interest(p,t,r):
    return (p*t*r)/100
p,t,r=map(float,input().split())
print(simple_interest(p,t,r))