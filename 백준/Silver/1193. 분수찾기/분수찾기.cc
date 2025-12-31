#include <stdio.h>
int main() {
	int X; scanf("%d", &X);
	int i = 1; for (; X > i; i++) X -= i;
	i % 2 == 0 ? printf("%d/%d", X, i - X + 1) : printf("%d/%d", i - X + 1, X);
}