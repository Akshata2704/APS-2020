# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:25:28 2020

@author: AKSHATA
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:17:36 2020

@author: AKSHATA
"""

N=int(input())
for _ in range(N):
    n=int(input())
    a=list(map(int,input().split()))
    a=sorted(a)
    a.reverse()
    p=0
    i=0
    while(i<n):
        k=a[i]-i
        if(k>0):
            p+=k
            i+=1
        else:
            i=n
    print(p%((10**9)+7))
    
    