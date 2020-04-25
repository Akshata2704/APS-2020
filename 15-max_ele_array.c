#include<stdio.h>
#include<limits.h>
int main()
{
    int arr[100],n,i,max=INT_MIN;
    printf("Enter number of elemnts:");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
        if(arr[i]>max)
            max=arr[i];
    }


    printf("Smallent number is %d",max);
}
