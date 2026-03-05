#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int main() {
	int n, i = 0, c = 1; cin >> n;
	vector<int> v(n); for (int j = 0; j < n; ++j) cin >> v[j];
	stack<int> s; while (i < n || !s.empty()) {
		if (!s.empty() && s.top() == c) { s.pop(); c++; }
		else if (i < n) {
			if (v[i] == c) { c++; i++; }
			else s.push(v[i++]);
		} else break;
	} cout << (c - 1 == n ? "Nice" : "Sad");
}