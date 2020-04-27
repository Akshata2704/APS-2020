#include<stdio.h>
#include<string.h>
int max(int a,int b)
{
    if(a>b)
        return a;
    else
        return b;

}

int max_subseq(char *a,char *b,int n1,int n2)
{
 int lcs[n1+1][n2+1],i,j,k;
 char array[200];
 for(i=0;i<=n1;i++)
        lcs[i][0]=0;
 for(i=0;i<=n2;i++)
    lcs[0][i]=0;
    k=0;
 for(i=0;i<n1;i++)
 {
     for(j=0;j<n2;j++)
     {
         if(a[i]==b[j])
         {


             lcs[i+1][j+1]=lcs[i][j]+1;


         }
         else
            lcs[i+1][j+1]=max(lcs[i][j+1],lcs[i+1][j]);
     }
 }

 return lcs[n1][n2];
}
int main()
{
 int n1,n2;
    char s1[100],s2[100];
    scanf("%s",s1);
    scanf(" %s",s2);
    n1=strlen(s1);
    n2=strlen(s2);
max_subseq(s1,s2,n1,n2);
    printf("%d",max_subseq(s1,s2,n1,n2));

}
