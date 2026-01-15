#include <iostream>
#include <string>
#include <map>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int N, M; cin >> N >> M; string* a = new string[N + 1]; map<string, int> m;
	for (int i = 1; i <= N; ++i) { cin >> a[i]; m[a[i]] = i; }
	while (M--) {
		string t; cin >> t;
		if (isdigit(t[0])) cout << a[stoi(t)] << '\n'; else cout << m[t] << '\n';
	}
}