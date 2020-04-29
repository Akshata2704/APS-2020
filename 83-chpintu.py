import sys
t=int(input())
while(t):
    n,m=map(int,input().split())
    types=list(map(int,input().split()))
    cost=list(map(int,input().split()))
    a=[0 for _ in range(m+1)]
 
    for i in range(m+1):
        if(i not in types):
            a[i]=sys.maxsize
    for j in range(len(types)):
        a[types[j]]+=cost[j]
 
    print(min(a))
    t-=1