#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int arr[9][9];
	int r=0, c=0, max=0;
	
	for(int i=0;i<9;i++)
	{
		for(int j=0;j<9;j++)
		{
			scanf("%d",&arr[i][j]);
			if(max<arr[i][j])
			{
				max=arr[i][j];
				r=i;
				c=j;
			}
		}
	}
	
	printf("%d\n",max);
	printf("%d %d",r+1,c+1);
	
	return 0;
}