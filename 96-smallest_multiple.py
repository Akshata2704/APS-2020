#!/bin/python3



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fl=0
    i=n
    while(fl==0):
     
        fl1=0
        j=2
        while(fl1==0 and j<=n):
          
            if(i%j!=0):
                i+=1
                fl1=1
            else:
                j+=1
        if(j==n+1):
            print(i)
            fl=1
                
       
