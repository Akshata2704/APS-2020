# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:26:34 2020

@author: AKSHATA
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:24:02 2020

@author: AKSHATA
"""

for _ in range(int(input())):
    N=int(input())
    if(N==1):
        print(1)
        print(1,end=" ")
        print(1)
    else:
        print(N//2)
        if(N&1):
            print(3,end=" ")
            print(1,end=" ")
            print(2,end=" ")
            print(3,end="\n")
            
            j=4
            while(j<=N):
                print(2,end=" ")
                print(j,end=" ")
                print(j+1,end="\n")
                j+=2
          
                
        else:
            j=1
            while(j<=N-1):
                print(2,end=" ")
                print(j,end=" ")
                print(j+1)
                j+=2
                
            