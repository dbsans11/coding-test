#include <bits/stdc++.h>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int N, M; cin >> N >> M; vector<string> v1(N), v2(M); 
	for (int i = 0; i < N; ++i) cin >> v1[i]; for (int i = 0; i < M; ++i) cin >> v2[i]; 
	sort(v1.begin(), v1.end()); sort(v2.begin(), v2.end());
	vector<string> r; auto t = set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), back_inserter(r));
	cout << r.size() << '\n'; for (string n : r) cout << n << '\n';
}