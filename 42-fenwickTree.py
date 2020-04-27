# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:38:36 2020

@author: AKSHATA
"""

fenwick=[0 for _ in range(100)]
a=[]
n=5 
def update(i,val):
    global n
    global fenwick
    while(i<=n):
      fenwick[i]+=val;
        i+=i & (-i)
        
def qry(i):
    global fenwick
    global n
    qrysum=0
    while(i>0):
        qrysum+=fenwick[i]
        i-=i&(-i)
    return qrysum



i=0
a=[1,2,3,4,5]
while(i<n):   
    update(i+1,a[i])
    i+=1

p=int(input())
q=int(input())
print(qry(q)+qry(p-1))
    
    