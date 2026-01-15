#include <iostream>
#include <string>
#include <map>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int N, M; map<int, string> mp1; map<string, int> mp2; cin >> N >> M; for (int i = 1; i <= N; ++i) { cin >> mp1[i]; mp2[mp1[i]] = i; }
	while (M--) {
		string t; cin >> t; 
		try { cout << mp2.at(t) << '\n'; } catch (out_of_range) { cout << mp1.at(stoi(t)) << '\n'; }
	}
}