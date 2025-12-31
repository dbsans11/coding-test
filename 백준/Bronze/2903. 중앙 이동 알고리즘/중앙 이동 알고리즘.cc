#include <stdio.h>
int main() {
	int N, n = 2; scanf("%d", &N);
	while (N--) n += n - 1;
	printf("%d", n * n);
}