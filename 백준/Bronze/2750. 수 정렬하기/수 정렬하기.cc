#include <iostream>
using namespace std;
int main() {
	int N; cin >> N; int* a = new int[N]; for (int i = 0; i < N; ++i) cin >> a[i];
	for (int i = 1; i < N; ++i) {
		int k = a[i], j = i - 1; while (j >= 0 && a[j] > k) { a[j + 1] = a[j]; j--; }
		a[j + 1] = a[j]; a[j + 1] = k;
	} for (int i = 0; i < N; ++i) cout << a[i] << '\n';
}