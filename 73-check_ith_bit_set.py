# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:15:30 2020

@author: AKSHATA
"""

n=int(input())
k=int(input())
if(n&(1<<k)):
    print("YES")
else:
    print("NO")