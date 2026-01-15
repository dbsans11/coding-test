#include <iostream>
#include <string>
#include <map>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int N, M, s = 0; map<string, int> mp; cin >> N >> M; while (N--) { string t; cin >> t; mp[t] = 1; }
	while (M--) { string t; cin >> t; s += mp.count(t); } cout << s;
}