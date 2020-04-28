# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:33:52 2020

@author: AKSHATA
"""

def is_anagram(a,b):
    a=list(a)
    b=list(b)
    if(len(a)!=len(b)):
        return 0
    else:
        a=sorted(a)
        b=sorted(b)
        for i in range(0,len(a)):
            if(a[i]!=b[i]):
                return 0
        return 1
        
a=input()
b=input()
if(is_anagram(a,b)):
    print("YES")
else:
    print("NO")
    