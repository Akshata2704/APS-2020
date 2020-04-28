# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:45:12 2020

@author: AKSHATA
"""

def find(arr,leng,s):
    for i in range(1,2**leng):
        su=0
        for j in range(0,leng):
            if(((i>>j)&1)):
                su+=arr[j]
        if(su==s):
            print("YES")
            return
    print("NO")
    
    
su=5
n=4
arr=[-1,2,4,121]
find(arr,n,su)