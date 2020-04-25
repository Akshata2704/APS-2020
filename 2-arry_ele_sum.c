#include<stdio.h>
int main()
{

    int arr[50],i,n,sum=0;
    printf("Enter the number of array elements:");
    scanf("%d",&n);
    printf("Enter array elements\n");
    for(i=0;i<n;i++){
            scanf("%d",&arr[i]);
        sum=sum+arr[i];
    }
    printf("Sum of elements of array=%d",sum);

    return 0;
}
