#include <stdio.h>
int main(void)
{
	int sbmt[28];
	int i, num=1;

	for(i=0;i<28;i++)
		scanf("%d",&sbmt[i]);
	
	for(num=1;num<=30;num++)
	{
		for(i=0;i<28;i++)
		{
			if(num==sbmt[i])
				break;
			else if(i==27)
				printf("%d\n",num);
		}
	}
	
	return 0;
	
}