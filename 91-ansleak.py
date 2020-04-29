

for _ in range(int(input())):
    n,m,k=input().split()
    n=int(n)
    m=int(m)
    k=int(k)
    f=[]
    o=0
    fl=0
    for _ in range(n):
 
        a=list(map(int,input().split()))
        s=list(set(a))
        if(len(s)>1):
            c=[a.count(s[i]) for i in range(len(s))] 
            f.append(s[c.index(max(c))])
        else:
            if(s[0]+1<=m):
                f.append(s[0]+1)
            else:
                f.append(s[0]-1)
                        
      
    for g in range(len(f)):
        print(f[g],end=" ")
    
    
        