# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:20:47 2020

@author: AKSHATA
"""

def maxlength(s):
    cnt=0
    c=0
    for i in s:
        if(i=='1'):
            c+=1
        else:
            if(cnt<c):
                cnt=c
            c=0
    if(cnt<c):
        cnt=c
    return cnt


for _ in range(int(input())):
    s=input()
    print(maxlength(s))