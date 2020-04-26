#include<stdio.h>
#include<stdlib.h>
void check(int a[15],int s);
int main()
{
int a[15],n,i;
printf("Enter size of array:");
scanf("%d",&n);
printf("Enter array elements:");
for(i=0;i<n;i++)
{
    scanf("%d",&a[i]);

}
check(a,n);
}

void check(int a[15],int s)

{
    int p;
    for(p=1;p<s;p++)
    {
        if(a[p-1]>a[p])
        {
            printf("It doesnt represnt a tree in inorder");
            exit(0);
        }
    }
    printf("array represnts a tree in inorder");
}
