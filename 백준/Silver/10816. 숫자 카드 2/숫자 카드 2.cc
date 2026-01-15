#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int N, M; cin >> N; int* a = new int[N]; for (int i = 0; i < N; ++i) cin >> a[i];
	cin >> M; sort(a, a + N); while (M--) { int t; cin >> t; cout << upper_bound(a, a + N, t) - lower_bound(a, a + N, t) << ' '; }
}