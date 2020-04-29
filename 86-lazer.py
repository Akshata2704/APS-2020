# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:13:52 2020

@author: AKSHATA
"""

t = int(input())
for i in range(t):
    N,Q = [int(x) for x in input().split()]
    P = [int(x) for x in input().split()]
    b=[0 for _ in range(N)]
    for j in range(Q):
        cnt=0
        x1,x2,y = [int(x) for x in input().split()]
        pre=1
        for i in range(x1-2,min(x2+1,N)-1):
            y1=P[i]
            y2=P[i+1]
            x11=i+1
            pre=999
            x12=i+2          
            if(pre==999 or (y1-y2)*pre==-1):
                if((x1!=x12) and x2!=x11 and ((y>=y1 and y<=y2) or (y<=y1 and y>=y2))):
                    pre=y1-y2
                    cnt+=1
                    
        print(cnt)
                
            