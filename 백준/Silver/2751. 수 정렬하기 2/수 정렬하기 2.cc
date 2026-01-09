#include <iostream>
using namespace std;
int s[1000001];

void merge(int a[], int l, int m, int r) {
	int i = l, j = m + 1, k = l;
	while (i <= m && j <= r) s[k++] = a[i] <= a[j] ? a[i++] : a[j++];
	if (i > m) for (int n = j; n <= r; ++n) s[k++] = a[n];
	else for (int n = i; n <= m; ++n) s[k++] = a[n];
	for (int n = l; n <= r; ++n) a[n] = s[n];
}

void merge_sort(int a[], int l, int r) {
	if (l < r) {
		int m = (l + r) / 2;
		merge_sort(a, l, m); merge_sort(a, m + 1, r); merge(a, l, m, r);
	}
}

int main() {
	int N; cin >> N; int* a = new int[N]; for (int i = 0; i < N; ++i) cin >> a[i];
	merge_sort(a, 0, N - 1); for (int i = 0; i < N; ++i) cout << a[i] << '\n';
}