# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:16:49 2020

@author: AKSHATA
"""



def sumMatrix(n1, m1, n2, m2, arr1, arr2):
    if(n1!=n2 or m1!=m2):
        print("-1")
        
    else:
        k=[0 for i in range (n1*m1)]
        p=0
        for i in range(n1):
            for j in range(m1):
                k[p]=arr1[i][j]+arr2[i][j]
                p+=1
        for i in range(len(k)):
            print(k[i],end=" ")
            
            
for _ in range(int(input())):
    n1,m1=map(int,input().split())
    arr1=[[0 for _ in range(m1)] for _ in range(n1)]
    list1=list(map(int,input().split()))
    k=0
    for i in range(n1):
        for j in range(m1):
            arr1[i][j]=list1[k]
            k+=1
    k=0
    n2,m2=map(int,input().split())
    arr2=[[0 for _ in range(m2)] for _ in range(n2)]
    list2=list(map(int,input().split()))
    for i in range(n2):
        for j in range(m2):
            arr2[i][j]=list2[k]
            k+=1
    sumMatrix(n1,m1,n2,m2,arr1,arr2)
    print()
    