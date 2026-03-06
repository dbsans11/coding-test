#include <stdio.h>
int p[31][31];
int pascal(int n, int k) {
	if (k == 0 || n == k) return 1;
	if (p[n][k] != 0) return p[n][k];
	return p[n][k] = pascal(n - 1, k) + pascal(n - 1, k - 1);
}
int main() {
	int t; scanf("%d", &t); while (t--) {
		int n, m; scanf("%d%d", &n, &m); printf("%d\n", pascal(m, n));
	}
}