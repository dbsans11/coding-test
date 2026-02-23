#include <stdio.h>
#include <math.h>
bool is_prime(long long n) {
	if (n == 1) return false;
	else if (n == 2) return true;
	else if (n % 2 == 0) return false;

	long long limit = sqrt(n);
	for (long long i = 3; i <= limit; i += 2) { if (n % i == 0) return false; }
	return true;
}

int main() {
	int t; scanf("%d", &t);
	while (t--) {
		long long temp; scanf("%lld", &temp);
		while (!is_prime(temp)) ++temp;
		printf("%lld\n", temp);
	}
}