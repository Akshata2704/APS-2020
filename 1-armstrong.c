#include<stdio.h>
int main()
{

    int n,i,sum=0,duplicate,rem;
    printf("Enter the number:");
    scanf("%d",&n);
    duplicate=n;
    while(n>0)
    {
        rem=n%10;
        sum=sum+(rem*rem*rem);
        n=n/10;

    }
    if(sum==duplicate)
        printf("It is a armstrong number");
    else
        printf("It is not a armstrong number");
            return 0;
}
