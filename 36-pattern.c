#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n,i,j,c,t,m,n1;
    scanf("%d",&n);

 t=n*2-1;
 int *a[t];
for(i=0;i<t;i++)

    a[i]=(int*)malloc(t*sizeof(int));


    c=t-1;

    for(i=0;i<t;i++)
    {
        for(j=i;j<t-i;j++)
        {

            a[i][j]=n;
            a[c][j]=n;
            a[j][i]=n;
            a[j][c]=n;

        }
        c--;
            n--;



    }
             for(m=0;m<t;m++){
for(n1=0;n1<t;n1++){
    printf("%d ",a[m][n1]);
}
printf("\n");
}


}
