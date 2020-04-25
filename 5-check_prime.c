#include<stdio.h>

int main()
{

    int n,i;
    printf("Enter the number:");
    scanf("%d",&n);
    for(i=2;i<=(n/2);i++)
    {
        if(n%i==0){
            printf("The number is not prime");
            return 0;
        }
    }
    printf("The number is prime");
}
