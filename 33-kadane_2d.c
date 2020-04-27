
#include <stdio.h>
#include <string.h>
#include <limits.h>
int ROW,COL;


int kadane(int* arr, int* start, int* finish, int n)
{
	
	int sum = 0, maxSum = INT_MIN, i;

	
	*finish = -1;


	int local_start = 0;

	for (i = 0; i < n; ++i)
	{
		sum += arr[i];
		if (sum < 0)
		{
			sum = 0;
			local_start = i+1;
		}
		else if (sum > maxSum)
		{
			maxSum = sum;
			*start = local_start;
			*finish = i;
		}
	}


	if (*finish != -1)
		return maxSum;


	maxSum = arr[0];
	*start = *finish = 0;

	for (i = 1; i < n; i++)
	{
		if (arr[i] > maxSum)
		{
			maxSum = arr[i];
			*start = *finish = i;
		}
	}
	return maxSum;
}


void findMaxSum(int M[][COL])
{
	
	int pq,rs,cnt=0;
	int maxSum = INT_MIN, finalLeft, finalRight, finalTop, finalBottom;

	int left, right, i;
	int temp[ROW], sum, start, finish;

	
	for (left = 0; left < COL; ++left)
	{
	
		memset(temp, 0, sizeof(temp));

		
		for (right = left; right < COL; ++right)
		{

			for (i = 0; i < ROW; ++i)
				temp[i] += M[i][right];

		
			sum = kadane(temp, &start, &finish, ROW);

			if (sum > maxSum)
			{
				maxSum = sum;
				finalLeft = left;
				finalRight = right;
				finalTop = start;
				finalBottom = finish;
			}
		}
	}

	// Print final values
	printf("(Top, Left) (%d, %d)\n", finalTop, finalLeft);
	printf("(Bottom, Right) (%d, %d)\n", finalBottom, finalRight);
	printf("Max sum is: %d\n", maxSum);
	for(pq=finalTop;pq<=finalBottom;pq++)
    {

        for(rs=finalLeft;rs<=finalRight;rs++)
        {
            if(M[pq][rs]<0)
            {
                cnt+=M[pq][rs]*(-1);
            }
        }
    }
    printf("%d",maxSum+cnt);

}


int main()
{
    int M[ROW+1][COL+1];
      int i,j;
    scanf("%d %d",&ROW,&COL);
printf("%d %d\n",ROW,COL);
    for(i=0;i<ROW;i++)
    {
        for(j=0;j<COL;j++)
        {
            scanf("%d",&M[i][j]);
        }
    }
      for(i=0;i<ROW;i++)
    {
        for(j=0;j<COL;j++)
        {
            printf("%d\t",M[i][j]);
        }
        printf("\n");
    }


	findMaxSum(M);

	return 0;
}
