#define _CPT_SECURE_NO_WARNING
#include <stdio.h>

int main(void)
{
	char ch[5][15]={0};
	
	for(int i=0;i<5;i++)
		scanf("%s",ch[i]);

	for(int i=0;i<15;i++)
	{
		for(int j=0;j<5;j++)
		{
			if(ch[j][i]!='\0')
				printf("%c",ch[j][i]);
			else
				continue;
		}
	}
	
	return 0;
}