#include<stdio.h>
int main()
{
    char a;
    printf("Enter the character:");
    scanf("%c",&a);
    if(a>=65 && a<91)
        a=a|32;
    printf("Lower case of character is %c",a);
    return 0;
}
