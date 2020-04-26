#include<stdio.h>
#include<stdlib.h>

void check(int ar[15],int n)
{
    int i,j,k,m;
    j=1;
    i=ar[0];
    while(ar[j]<i && j<n)
    {
        j++;
    }
    if(j==n)
    {
        printf("doesnt represnt preorder");
        exit(0);
    }
    else
{

    k=ar[j];
    for(m=j+1;m<n;m++)
    {
        if(ar[m]<i)
        {
            printf("doesnt represnt preorder");
            exit(0);
        }
    }
    printf("Represents preorder");

}
}


main()
{
    int ar [15],h,g;
    printf("Enter size:");
    scanf("%d",&g);
    printf("Enter elements:");
    for(h=0;h<g;h++)
        scanf("%d",&ar[h]);
    check(ar,g);
}
