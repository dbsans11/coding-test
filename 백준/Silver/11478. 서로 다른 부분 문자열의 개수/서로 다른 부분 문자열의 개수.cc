#include <iostream>
#include <string>
#include <set>
using namespace std;
int main() {
	string s; cin >> s; int l = s.length(); set<string> r;
	for (int i = 0; i <= l; ++i) for (int j = 1; j <= l - i; ++j) r.insert(s.substr(i, j)); cout << r.size();
}