#include <stdio.h>
int main(void)
{
	int arr[10];
	int i, j, num=1;
	for(i=0;i<10;i++)
	{
		scanf("%d",&arr[i]);
		arr[i]%=42;
	}
		
	for(i=0;i<10;i++)
	{
		for(j=i+1;j<10;j++)
		{
			if(arr[i]==arr[j])
				break;
			else if(j==9)
				num++;
		}
	}
	printf("%d",num);
	
	return 0;
	
}