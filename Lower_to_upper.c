#include<stdio.h>
int main()
{
    char a;
    printf("Enter the character:");
    scanf("%c",&a);
   if(a>=97 && a<=122)
       a=a & (~32);
    printf("Upper case of character is %c",a);
    return 0;
}
