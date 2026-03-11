#include <iostream>
using namespace std;

int cnt, k, res = -1;
int* tmp;

void merge(int* a, int p, int q, int r) {
	int i = p, j = q + 1, t = 0;
	while (i <= q && j <= r) {
		tmp[t++] = (a[i] <= a[j] ? a[i++] : a[j++]);
	} while (i <= q) tmp[t++] = a[i++]; while (j <= r) tmp[t++] = a[j++];
	t = 0; for (int n = p; n <= r; ++n) {
		a[n] = tmp[t++]; if (++cnt == k) res = a[n];
	}
}

void merge_sort(int* a, int p, int r) {
	if (p < r) {
		int q = (p + r) / 2;
		merge_sort(a, p, q); merge_sort(a, q + 1, r); merge(a, p, q, r);
	}
}

int main() {
	int n; cin >> n >> k; int* a = new int[n]; tmp = new int[n]; 
	for (int i = 0; i < n; ++i) cin >> a[i];
	merge_sort(a, 0, n - 1); cout << res;
}