#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int count[10]={0},j,n,k;
    char a[1000],i;


    scanf("%s",a);
    n=strlen(a);
    

    for(i='0',k=0;i<='9',k<=9;i++,k++)
    {
        for(j=0;j<n;j++)
        {
            if(a[j]==i)
            {


            count[k]=count[k]+1;
        
            }
        }
    }
    for(j=0;j<=9;j++)
    printf("%d ",count[j]);


    return 0;
}

