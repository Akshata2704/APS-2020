#include<stdio.h>

int main()
{
	int t,n,m,i,g;
	int co,ce;

	scanf("%d",&t);
	while(t)
    {
	scanf("%d %d",&m,&n);
	co=0;
	ce=0;


	int Q[m];
	for(i=0;i<m;i++)
    {
    scanf("%d",&Q[i]);
	if(__builtin_parityll(Q[i]))
        co+=1;
    else
    ce+=1;

	}

	for(i=0;i<n;i++)
    {
        scanf("%d",&g);
        if(__builtin_parityll(g))
        {
             printf("%d %d\n",co,ce);
        }
        else
            printf("%d %d\n",ce,co);
    }
    t-=1;
    }
}
