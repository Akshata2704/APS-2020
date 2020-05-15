def substr(a,b):
    a1=len(a)
    b1=len(b)
    res=0
    lcs=[[0 for _ in range(b1+1)]  for _ in range(a1+1)]
    for i in range(a1+1):
        for j in range(b1+1):
            if(i==0 or j ==0):
                lcs[i][j]=0
            else:
                if(a[i-1]==b[j-1]):
                    lcs[i][j]=lcs[i-1][j-1]+1
                    res=max(res,lcs[i][j])
                else:
                    lcs[i][j]=0
    return res
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=input()
    b=input()
    print(substr(a,b))
    