

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:40:56 2020

@author: AKSHATA
"""
m=[]
res=[]
t=int(input())
if(1<=t<=10000):
    while(t):
        np=input().split()
        N=int(np[0])
        P=int(np[1])
        if(1<=N<=1000 and 1<=P<=1000000000):
           
            c=[]
 
            pre=10000
            arr=list(map(int,input().split()))
            q=sorted(arr)
            if(arr==q):
                cntt=0
                cnttt=0
                flag=0
                for i in range(N):
                    if(P%arr[i]==0):
                        cntt+=1
                        for j in range(i):
                            if(arr[i]%arr[j]!=0):
                                flag=1
                
                if(cntt==N and flag==0):
                   res.append(0)
                else:
                    cnt=[0 for i in range(N)]
                    i=len(arr)-1
                    fl=0
                    if(arr[i]>P):
                        cnt[i]=1;
                    else:
                        temp=0
                        if(cntt==N):
                            
                            
                            S=0
                        
                            j=(len(arr)-1)
                            E=P
                            while(j>=0 and S<P):
                                q=int(E%arr[j]);
                                if(q==0):
                                    temp=S+(arr[j]*((E/arr[j])-1));cnt[j]+=int((E/arr[j])-1)
                                else:
                                    temp=S+(arr[j]*(int(E/arr[j])+1));cnt[j]+=(int(E/arr[j])+1)
                              
                                fl=0
                                
                                if(temp>P):
                                    if(temp-arr[j]>=P):
                                        fl=1
                                    
                                if(fl==0 and (temp<P or (temp>P and S<P))):
                                    S=temp;
                                    E=P-S
                                    
                            
                                j-=1;
                        else:
                            temp=0
                            S=0
                            j=(len(arr)-1)
                            E=P
                            while(j>=0 and S<P):
                                if(P%arr[j]!=0):
                                    q=int(E%arr[j]);
                                    if(q==0):
                                        temp=S+(arr[j]*((E/arr[j])-1));cnt[j]+=int((E/arr[j])-1)
                                    else:
                                        temp=S+(arr[j]*(int(E/arr[j])+1));cnt[j]+=(int(E/arr[j])+1)
                              
                                    fl=0
                                
                                    if(temp>P):
                                        if(temp-arr[j]>=P):
                                            fl=1
                                    
                                    if(fl==0 and (temp<P or (temp>P and S<P))):
                                        S=temp;
                                        E=P-S
                                    
                            
                                j-=1;
                            
                        
                        
                    res.append(1)
                    m.append(cnt)
        
                                
                        
                    
                    
                   
                        
        
        
        t-=1
    k=0
    for i in range(len(res)):
        if(res[i]==0):
            print("NO")
        else:
            print("YES",end=" ")
            for j in range(len(m[k])):
                if(j<(len(m[k])-1)):
                    print(m[k][j],end=" ")
                else:
                    print(m[k][j])
            k+=1

                        
                        
                        
                            
                    
                
                
                
                
               
                
                    
                    
               
                  
            
            
            
    
    
    

    
    