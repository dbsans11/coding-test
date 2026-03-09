#include <iostream>
#include <set>
#include <string>
using namespace std;
int main() {
	int n, r = 0; cin >> n; set<string> s; while (n--) {
		string t; cin >> t; if (t == "ENTER") { r += s.size(); s.clear(); } else s.insert(t);
	} cout << r + s.size();
}