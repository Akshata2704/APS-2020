#include<stdio.h>
#include<stdlib.h>
int max(int a,int b,int c)
{
    if(a>b && a>c)
    return a;
    else if(b>c)
        return b;
    else
        return c;

}
int rod_cutting(int n)
{
   int result[n+1],i,j;
   result[0]=0,result[1]=0;
   for(i=2;i<=n;i++)
   {
       result[i]=0;
       for(j=1;j<=(i/2);j++)
       {
          result[i]=max(result[i],(j*(i-j)),(j*result[i-j]));

       }
   }
   return result[n];

}
int main()
{
    int n,res;
    scanf("%d",&n);
    res=rod_cutting(n);
    printf("%d",res);
}
