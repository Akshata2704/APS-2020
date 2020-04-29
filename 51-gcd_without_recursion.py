# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:16:59 2020

@author: AKSHATA
"""
def gcd(a,b):
    num1=a
    num2=b
    while(num1%num2!=0):
        t=num1
        num1=num2
        num2=t%num2
    return num2
a,b=map(int,input().split())

print(gcd(a,b))