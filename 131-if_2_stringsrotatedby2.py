# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:40:47 2020

@author: AKSHATA
"""

#code
def posb(n,m):
    if(len(n)!=len(m)):
        return 0
    if(n[0]==m[len(n)-2]):
        for i in range(2,len(n)):
            if(n[i]!=m[i-2]):
                return 0
        
        return 1
    elif(m[0]==n[len(n)-2]):
        for i in range(2,len(n)):
            if(m[i]!=n[i-2]):
                return 0
        return 1
    else:
        return 0
        
for _ in range(int(input())):
    n=input()
    m=input()
    if(posb(n,m)):
        print(1)
    else:
        print(0)