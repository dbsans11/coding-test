#include <stdio.h>
int fact(int n) { int r = 1; for (int i = 2; i <= n; ++i) r *= i; return r; }
int main() {
	int n, k; scanf("%d%d", &n, &k); printf("%d", fact(n) / (fact(n - k) * fact(k)));
}