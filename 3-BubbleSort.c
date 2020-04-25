#include<stdio.h>
int main()
{

    int i,j,arr[20],n,temp;
    printf("Enter the size of array :");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    scanf("%d",&arr[i]);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(arr[j]>arr[j+1])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    printf("After sorting:");
    for(i=0;i<n;i++)
        printf("%d,",arr[i]);

}
