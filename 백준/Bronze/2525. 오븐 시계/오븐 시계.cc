#include <stdio.h>
int main() {
	int A, B, C; scanf("%d %d %d", &A, &B, &C);
	B += C; A += B / 60; B %= 60;
	printf("%d %d", A >= 24 ? A - 24 : A, B);
}