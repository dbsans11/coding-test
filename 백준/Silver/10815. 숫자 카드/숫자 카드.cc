#include <iostream>
#include <map>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int N, M; map<int, int> m; cin >> N; for (int i = 0; i < N; ++i) { int t; cin >> t; m[t] = 1; }
	cin >> M; for (int i = 0; i < M; ++i) { int t; cin >> t; cout << m[t] << ' '; }
}