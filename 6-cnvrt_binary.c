#include<stdio.h>
int main()
{
    int n,i=0,re,sum[20],j;
    printf("Enter the decimal number:");
    scanf("%d",&n);
    while(n>0)
    {
        re=n%2;
        sum[i]=re;
        i++;
        n=n/2;

    }
    printf("Binary form of number is:");
    for(j=i-1;j>=0;j--)
        printf("%d",sum[j]);

}

