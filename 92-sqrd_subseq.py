# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:53:13 2020

@author: AKSHATA
"""


def check(n,lst):  
    count=0 
    pre=-1
    i=0
    while(i<n):
       
        h=lst[i]
   
   
        if(h&1):
            
           
            j=i+1
            s=1
            while(j<n and lst[j]&1):
                j+=1
                s+=1
        
                
            count+=int((s*(s+1))/2)
            i=j
           
          
        else:
            if( h%4==0 and i>pre):
                count+=1
                count+=(i-pre-1)+((n-1)-i)+((i-pre-1)*(n-1-i))
             
                pre=i
                
             
            else:
                if(h%2==0 and i+1<n):
                    
                    j=i+1
                    while(j<n and lst[j]&1):
                        j+=1
                    
                    if(j<n and lst[j]%4!=0):
                        count+=1
                        count+=(i-pre-1)+(n-1-j)+((i-pre-1)*(n-1-j))
                        pre=i
            i+=1
                     
    return count
                        
                
            
        
        
             
t=int(input())
for i in range(t):
    n=int(input())
    h=list(map(int,input().split()))
 
    res=check(n,h)
    print(res)