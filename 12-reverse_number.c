#include<stdio.h>
int main()
{
    int n,i,rem,sum=0;
    printf("enter the number:");
    scanf("%d",&n);
    while(n>0)
    {
        rem=n%10;
        sum=(sum*10)+rem;
        n=n/10;
    }
    printf("Reversed number is %d",sum);
}
