#python 3


t=int(input())
if(1<=t<=50):
    final=[]
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split(' ')))
        b=list(map(int,input().split(' ')))
        
        a=sorted(a)
        b=sorted(b)
        
        i=0
        array=[]
        for i in range(n):
            array.append(min(a[i],b[i]))
        final.append((sum(array)))
      


    for i in range(0,t):
        print(final[i])
    
   

    
    
