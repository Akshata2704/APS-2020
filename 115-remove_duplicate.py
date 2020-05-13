def remove_duplicate(n, arr):
    i=0
    while(i<n-1):
        j=i+1
        while(j<n and arr[j]==arr[i]):
            arr.remove(arr[j])
            n-=1
        i=j
    return len(arr)
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    n=remove_duplicate(n,arr)
    for i in range(n):
        print(arr[i],end=" ")
    print()