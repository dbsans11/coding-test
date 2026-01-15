#include <iostream>
#include <algorithm>
using namespace std;

bool binary_search(int a[], int s, int k) {
	int l = 0, h = s - 1;
	while (l <= h) {
		int m = (l + h) / 2; if (k == a[m]) return 1;
		if (k < a[m]) h = m - 1; else l = m + 1;
	} return 0;
}

int main() {
	int N, M; cin >> N; int* a = new int[N]; for (int i = 0; i < N; ++i) cin >> a[i];
	sort(a, a + N); cin >> M; int* r = new int[M]; for (int i = 0; i < M; ++i) cin >> r[i];
	for (int i = 0; i < M; ++i) cout << binary_search(a, N, r[i]) << ' ';
}