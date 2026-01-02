#include <stdio.h>
int main() {
	int N, res = 0; scanf("%d", &N);
	while (N--) { int t; scanf("%1d", &t); res += t; }
	printf("%d", res);
}