#include <iostream>
#include <map>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int N; map<int, int> m; cin >> N; while (N--) { int t; cin >> t; m[t] += 1; }
	cin >> N; while (N--) { int t; cin >> t; cout << m[t] << ' '; }
}