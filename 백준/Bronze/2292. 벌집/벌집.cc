#include <stdio.h>
int main() {
	int N; scanf("%d", &N);
	int cnt = 1; N -= cnt;
	while (N > 0) N -= cnt++ * 6;
	printf("%d", cnt);
}