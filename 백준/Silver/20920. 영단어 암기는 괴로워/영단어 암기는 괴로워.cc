#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

map<string, int> m;

bool cmp(string a, string b) {
	if (m[a] != m[b]) return m[a] > m[b];
	if (a.length() != b.length()) return a.length() > b.length();
	return a < b;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(NULL);
	int N, M; cin >> N >> M; vector<string> v; while (N--) {
		string s; cin >> s; if (s.length() < M) continue;
		v.push_back(s); m[s]++;
	} sort(v.begin(), v.end(), cmp); v.erase(unique(v.begin(), v.end()), v.end());
	for (string s : v) cout << s << '\n';
}