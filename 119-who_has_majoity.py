# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:29:30 2020

@author: AKSHATA
"""

def majorityWins(arr, n,  x,y):
    cx=0
    cy=0
    for i in range(n):
        if(arr[i]==x):
            cx+=1
        if(arr[i]==y):
            cy+=1
    if(cx>cy):
        return x
    elif(cy>cx):
        return y
    else:
        return min(x,y)
    
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    x,y=map(int,input().split())
    print(majorityWins(arr,n,x,y))
    