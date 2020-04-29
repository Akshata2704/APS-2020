t=int(input())
while(t):
    n=int(input())
    dictk={}
    for _ in range(n):
        s,h=(input().split())
        if(s not in dictk):
            dictk[s]=[]
            dictk[s].append(int(h))
        else:
            dictk[s].append(int(h))

    count=0
    for key in dictk:
        k=dictk[key].count(1)
        j=dictk[key].count(0)
        if(k>j):
            count+=k
        else:
            count+=j
    print(count)
    t-=1;
    
    
    