#include <iostream>
#include <string>
#include <set>
using namespace std;
int main() {
	int n; set<string> s; cin >> n;
	while (n-- > 0) { 
		string t, b; cin >> t >> b;
		if (b == "enter") s.insert(t); else s.erase(t);
	} for (auto i = s.rbegin(); i != s.rend(); ++i) cout << *i << '\n';
}