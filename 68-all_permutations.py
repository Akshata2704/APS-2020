# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:25:19 2020

@author: AKSHATA
"""

n=int(input())
num=list(map(int,input().split(' ')))
print(num)

for j in range(1,n+1):
    for i in range(0,n-1):
        temp=num[i]
        num[i]=num[i+1]
        num[i+1]=temp;
        print(num)
        
      