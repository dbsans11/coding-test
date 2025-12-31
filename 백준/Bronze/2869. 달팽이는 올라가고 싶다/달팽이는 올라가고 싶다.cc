#include <stdio.h>
int main() {
	int A, B, V; scanf("%d %d %d", &A, &B, &V);
	V -= A; A -= B; V% A == 0 ? printf("%d", 1 + V / A) : printf("%d", 2 + V / A);
}