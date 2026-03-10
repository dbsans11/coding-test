#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;
int main() {
	int n; cin >> n; unordered_set<string> s; s.insert("ChongChong");
	while (n--) {
		string a, b; cin >> a >> b;
		if (s.find(a) != s.end()) s.insert(b); else if (s.find(b) != s.end()) s.insert(a);
	} cout << s.size();
}