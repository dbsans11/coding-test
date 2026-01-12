#include <iostream>
using namespace std;
int main() {
	int N; cin >> N; int* a = new int[N]; for (int i = 0; i < N; ++i) cin >> a[i];
	for (int i = N - 1; i > 0; --i) {
		for (int j = 0; j < i; ++j) if (a[j] > a[j + 1]) swap(a[j], a[j + 1]);
	} for (int i = 0; i < N; ++i) cout << a[i] << '\n';
}