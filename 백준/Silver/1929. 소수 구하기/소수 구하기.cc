#include <iostream>
using namespace std;
bool is_prime(int n) {
	if (n == 2) return 1; else if (n == 1 || n % 2 == 0) return 0;
	for (int i = 3; i * i <= n; i += 2) if (n % i == 0) return 0; return 1;
}
int main() {
	int m, n; cin >> m >> n; for (int i = m; i <= n; ++i) if (is_prime(i)) cout << i << '\n';
}