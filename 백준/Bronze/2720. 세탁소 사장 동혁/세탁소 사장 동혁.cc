#include <stdio.h>
int main() {
	int T; scanf("%d", &T);
	int coins[] = { 25, 10, 5, 1 };
	while (T--) {
		int C; scanf("%d", &C);
		for (int i = 0; i < 4; ++i) {
			printf("%d ", C / coins[i]);
			C %= coins[i];
		} printf("\n");
	}
}
