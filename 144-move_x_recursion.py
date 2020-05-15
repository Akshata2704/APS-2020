# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:53:42 2020

@author: AKSHATA
"""
def mov(s,l,h):
    if(l>=h):
        return
    sw=s[l]
    if(sw!='x'):
        print(s[l],end="")
    mov(s,l+1,h)
    if(sw=='x'):
        print('x',end="")
    return 


s=input()
mov(s,0,len(s))