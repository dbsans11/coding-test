#include <stdio.h>
int main(void)
{
	int N, temp=0, total=0;
	scanf("%d",&N);
	char arr[N];
	scanf("%s",arr);
	
	for(int i=0;i<N;i++)
		total+=arr[i]-'0';
	printf("%d",total);
	
	return 0;
	
}