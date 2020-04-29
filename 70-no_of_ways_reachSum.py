# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 08:03:29 2020

@author: AKSHATA
"""

n=int(input())
cnt=0;
r=[]
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            m=(3*i)+(5*j)+(10*k);
            if(m==n):
                for s in range(i):
                    r.append(3)
                for _ in range(j):
                    r.append(5);
                for _ in range(k):
                    r.append(10);
                cnt+=1;
                print(r)
                r.clear();
print(cnt)