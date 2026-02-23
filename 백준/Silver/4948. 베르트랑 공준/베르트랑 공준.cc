#include <iostream>
#include <algorithm>
using namespace std;
int a[246913] = { 0, 1 };
int main() {
	for (int i = 2; i <= 246913; ++i) for (int j = 2; i * j <= 246913; ++j) a[i * j] = 1;
	while (1) { int n; cin >> n; if (!n) break; cout << count(a + n + 1, a + 2 * n + 1, 0) << '\n'; }
}