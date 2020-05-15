# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:43:58 2020

@author: AKSHATA
"""
global s
def union(a,b):
    global s
    for i in range(len(s)):
        if(s[i]==a):
            s[i]=s[b]
            
def find(a,b):
    if(s[a]==s[b]):
        return True
    else:
        return False
    
s=[i for i in range(9)]
union(8,7)
union(2,4)
union(4,6)
print(find(2,6))
print(find(6,7))
            
    