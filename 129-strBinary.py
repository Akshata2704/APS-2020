# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:35:09 2020

@author: AKSHATA
"""
def isBinary(str):
    for i in str:
        if(not(i=='1' or i=='0')):
            return 0
    return 1
str=input()
if(isBinary(str)):
    print(1)
else:
    print(0)