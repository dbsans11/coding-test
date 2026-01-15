#include <bits/stdc++.h>
using namespace std;
int main() {
	ios::sync_with_stdio(0); cin.tie(NULL);
	int N, M; cin >> N >> M; vector<string> v(N), r; for (int i = 0; i < N; ++i) cin >> v[i];
	sort(v.begin(), v.end()); while (M--) { string t; cin >> t; if (binary_search(v.begin(), v.end(), t)) r.push_back(t); }
	sort(r.begin(), r.end()); cout << r.size() << '\n'; for (string t : r) cout << t << '\n';
}