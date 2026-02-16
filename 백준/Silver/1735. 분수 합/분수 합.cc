#include <stdio.h>

int gcd(int a, int b) {
	if (a < b) { int temp = a; a = b; b = temp; }
	while (b > 0) { int temp = a; a = b; b = temp % b; }
	return a;
}

int main() {
	int a1, a2, b1, b2;
	scanf("%d %d", &a1, &a2); scanf("%d %d", &b1, &b2);
	int res1 = a1 * b2 + b1 * a2, res2 = a2 * b2;
	int temp = gcd(res1, res2);
	printf("%d %d", res1 / temp, res2 / temp);
}