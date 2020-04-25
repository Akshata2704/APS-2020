#include<stdio.h>
int main()
{
    int n;
    printf("Enter number:");
    scanf("%d",&n);
    if(n%2!=0)
        printf("Number is odd");
    else
        printf("Number is not odd");
}
