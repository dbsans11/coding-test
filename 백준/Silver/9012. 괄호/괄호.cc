#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main() {
	int t; cin >> t; while (t--) {
		string s1; stack<char> s2; cin >> s1;
		for (char c : s1) {
			if (s2.empty()) s2.push(c);
			else {
				if (s2.top() == '(' && c == ')') s2.pop();
				else s2.push(c);
			}
		} cout << (s2.empty() ? "YES" : "NO") << '\n';
	}
}