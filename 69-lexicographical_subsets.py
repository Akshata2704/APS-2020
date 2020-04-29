# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:45:50 2020

@author: AKSHATA
"""

def cp(strt,n):
    for l in range(1,n+1):
        for i in range(0,n-l+1):
            j=i+l-1;
            for k in range(i,j+1):
                print(strt[k],end=" ")
            print("\n")
                
                
strt="abcde"
cp(strt,len(strt))