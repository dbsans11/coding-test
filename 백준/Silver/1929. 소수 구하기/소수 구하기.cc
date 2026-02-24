#include <iostream>
using namespace std;
int a[1000001] = { 0, 1 };
int main() {
	int m, n;
		for (int i = 2; i <= 1000001; ++i) {
			if (a[i]) continue;
			for (int j = 2; i * j <= 1000001; ++j) a[i * j] = 1;
		}
	cin >> m >> n; for (int i = m; i <= n; ++i) if (!a[i]) cout << i << '\n';
}