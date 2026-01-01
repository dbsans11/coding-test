#include <stdio.h>
int main(void)
{
	int N, M;
	int i, j, num, temp;
	scanf("%d %d",&N,&M);
	int bsk[N];
	for(num=0;num<N;num++)
		bsk[num]=num+1;
	
	for(;M>0;M--)
	{
		scanf("%d %d",&i,&j);
		i--, j--;
		while(i<j)
		{
			temp=bsk[i];
			bsk[i]=bsk[j];
			bsk[j]=temp;
			i++, j--;
		}
	}
	
	for(num=0;num<N;num++)
		printf("%d ",bsk[num]);
	
	return 0;
	
}