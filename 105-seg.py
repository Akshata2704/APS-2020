res=[]
def seg(e):
    c=0
    global res
    i=0
    while(i<len(e)):
        it=e[i][1]
        res.append(it)
        j=i+1
       
        while(j<len(e) and e[j][0]<=it):
            j+=1
          
        if(j==len(e)):
            c+=1
            return c
        else:
            i=j
            c+=1
            
n=int(input())
e=[]
d={}
den=[]
for _ in range(n):
    m,n=map(int,input().split())
    den.append(n)
    if(n in d):
        d[n].append(m)
    else:
        d[n]=[]
        d[n].append(m)
den=list(set(sorted(den)))
for i in range(len(den)):
    d[den[i]]=sorted(d[den[i]])
for i in range(len(den)):
    for j in range(len(d[den[i]])):
        e.append([d[den[i]][j],den[i]])
        
print(seg(e))
for i in range(len(res)):
    print(res[i], end=" ")
        