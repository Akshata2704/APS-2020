

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:07:48 2020

@author: AKSHATA
"""

from itertools import product
t=int(input())
if(1<=t<=5):
    for k in range(t):
    
        m,n=input().split()
        m=int(m)
        n=int(n)
        if(1<= m,n <= (10**5)):
            cnt=0
            x=list(map(int,input().split()))
            x1=[i  for i in x if i>0]
            x2=[i for i in x if i<0] 
            y=list(map(int,input().split()))
            y1=[i  for i in y if i>0]
            y2=[i for i in y if i<0] 
            if(0 in x):
                cnt+=((m-1)*n);
                x.remove(0)
                m=m-1
            elif(0 in y):
                cnt+=((n-1)*m);
                y.remove(0)
                n=n-1
        
 

   
  
    
            p1=list(product(x1,x2))
            p2=list(product(y1,y2))
           
            p1=[list(i) for i in p1]
            p2=[list(i) for i in p2]
         

    
    
  
   
            p1len=len(p1)
            p2len=len(p2)
        
            i=0;
         
            k=0
        
            while(i<p1len or k<p2len):
                j=0
                l=0
                while(j<n or l<m):
                    if(i<p1len and j<n):
                        
                        if(((-y[j])/p1[i][0])*((-y[j])/p1[i][1])==-1):
                            
                            cnt+=1
                    if(k<p2len and l<m):
                        
                         if(((p2[k][0]/(-x[l])))*((p2[k][1])/(-x[l]))==-1):
                        
                             cnt+=1
                    j+=1
                    l+=1
                i+=1
                k+=1
                        
                    
                        
            
                        
                       
                        
            print(cnt);
    
        k+=1

               
                
                
                
    
                
               
     
        
        
        
        
        
        
        
    



        
        
        
        
        
        
        
    
