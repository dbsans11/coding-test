#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	ios::sync_with_stdio(0); cin.tie(NULL);
	int N, M; cin >> N; int* a = new int[N]; for (int i = 0; i < N; ++i) cin >> a[i];
	cin >> M; int* r = new int[M]; for (int i = 0; i < M; ++i) cin >> r[i];
	sort(a, a + N); for (int i = 0; i < M; ++i) cout << binary_search(a, a + N, r[i]) << ' ';
}