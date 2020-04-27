#include<stdio.h>
int main()
{
    int n;
    printf("Enter the number to check:");
    scanf("%d",&n);
    if(n|0==1)
        printf("Number is odd");
}
