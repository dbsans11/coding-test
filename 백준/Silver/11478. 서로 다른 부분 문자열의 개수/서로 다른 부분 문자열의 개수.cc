#include <iostream>
#include <string>
#include <set>
using namespace std;
int main() {
	ios::sync_with_stdio(0); cin.tie(NULL);
	string s; cin >> s; int l = s.length(); set<string> r;
	for (int i = 0; i < l; ++i) for (int j = 1; j < l - i + 1; ++j) r.insert(s.substr(i, j)); cout << r.size();
}