# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:29:11 2020

@author: AKSHATA
"""
s=[1 for i in range(6)]

a=[0,1,2,3,4,5]
def root(b):
    global a
    while(a[b]==b):
        b=a[b];
    return b;

def union_find(u,v):
    global s
    global a
    rootu=root(u)
    rootv=root(v)
    if(s[rootu]<s[rootv]):
        a[rootv]=a[rootu];
        s[rootu]+=s[rootv]
    else:
        a[rootu]=a[rootv];
        s[rootv]+=s[rootu]


union_find(0,1)
print(a)
print(s)





        
    
    
    
    
    
    
