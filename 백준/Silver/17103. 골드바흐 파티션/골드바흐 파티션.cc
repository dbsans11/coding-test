#include <iostream>
using namespace std;
int a[1000001] = { 0, 1 };
int main() {
	for (int i = 2; i < 1000001; ++i) for (int j = 2; i * j < 1000001; ++j) a[i * j] = 1;
	int t; cin >> t; while (t--) {
		int n, s = 0; cin >> n; 
		for (int i = 2; i <= n / 2; ++i) if (!a[i] && !a[n - i]) ++s; cout << s << '\n';
	}
}