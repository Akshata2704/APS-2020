#!/bin/python3

import sys



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if(n<=3):
        print('0')
    else:
        N=(n-1)//3
        s=((N)*((6)+(N-1)*3))>>1;
        N=(n-1)//5;
        s2=((N)*((10)+(N-1)*5))>>1;
        s3=0
        if(n>15):
            N=(n-1)//15
          
            s3=((N)*((30)+((N-1)*15)))>>1
        sumt=s+s2-(s3)
      
        print(int(sumt))
        
        
         

    
