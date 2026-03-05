#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main() {
	while (1) {
		string s; getline(cin, s); if (s == ".") break;
		stack<int> t; for (char c : s) { 
			if (c == '(' || c == '[') t.push(c);
			else if (c == ')') {
				if (t.empty() || t.top() != '(') { t.push(c); break; }
				else t.pop();
			}
			else if (c == ']') {
				if (t.empty() || t.top() != '[') { t.push(c); break; }
				else t.pop();
			} 
		} cout << (t.empty() ? "yes" : "no") << '\n';
	}
}