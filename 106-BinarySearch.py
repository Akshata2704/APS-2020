#python 3
def binary_search(arr,k,n):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return mid;
        elif(k<arr[mid]):
            high=mid-1;
        else:
            low=mid+1;
    return -1
        

a=list(map(int,input().split()))
n=a[0]
arr=a[1:]
b=list(map(int,input().split()))
k=b[0]
brr=b[1:]
for i in range(k):
    print(binary_search(arr,brr[i],n),end=" ")
    