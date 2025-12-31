#include <stdio.h>
int main() {
	int N; scanf("%d", &N);
	int i = 1; N--;
	for (; N > 0; i++) N -= 6 * i;
	printf("%d", i);
}