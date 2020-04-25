#include<stdio.h>
int main()
{
    int n,result;
    printf("Enter the number:");
    scanf("%d",&n);
    result=fact(n);
    printf("Factorial of %d is %d",n,result);
    return 0;
}

int fact(int n)
{
    if(n==0)
        return 1;
    else if(n==1)
        return 1;
    else
        return (n*fact(n-1));
}
