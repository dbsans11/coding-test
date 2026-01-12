#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
bool cmp(pair<int, string>p1, pair<int, string>p2) { return p1.first < p2.first; }
int main() {
	int N; cin >> N; vector<pair<int, string>> v(N); for (int i = 0; i < N; ++i) cin >> v[i].first >> v[i].second;
	stable_sort(v.begin(), v.end(), cmp); for (int i = 0; i < N; ++i) cout << v[i].first << ' ' << v[i].second << '\n';
}