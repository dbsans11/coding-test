#include <iostream>
#include <stack>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	stack<int> s; int n; cin >> n; while (n--) {
		int f; cin >> f; switch (f) {
		case 1: int x; cin >> x; s.push(x); break;
		case 2:
			if (s.empty()) cout << -1 << '\n';
			else { cout << s.top() << '\n'; s.pop(); } break;
		case 3: cout << s.size() << '\n'; break;
		case 4: cout << s.empty() << '\n'; break;
		case 5: cout << (s.empty() ? -1 : s.top()) << '\n'; break;
		}
	}
}