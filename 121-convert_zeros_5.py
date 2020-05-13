# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:42:51 2020

@author: AKSHATA
"""

def convertFive(n):
    s=list(str(n))
    for i in range(len(s)):
        if(s[i]=='0'):
            s[i]='5'
            
    return ''.join(s)

for _ in range(int(input())):
    print(convertFive(int(input())))