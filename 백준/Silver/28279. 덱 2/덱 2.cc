#include <iostream>
#include <deque>
using namespace std;
int main() {
	ios::sync_with_stdio(0); cin.tie(NULL);
	int n; cin >> n; deque<int> dq; while (n--) {
		int c; cin >> c; switch (c) {
		case 1: int x; cin >> x; dq.push_front(x); break;
		case 2: int y; cin >> y; dq.push_back(y); break;
		case 3: if (dq.empty()) cout << "-1\n"; else { cout << dq.front() << '\n'; dq.pop_front(); } break;
		case 4: if (dq.empty()) cout << "-1\n"; else { cout << dq.back() << '\n'; dq.pop_back(); } break;
		case 5: cout << dq.size() << '\n'; break;
		case 6: cout << dq.empty() << '\n'; break;
		case 7: cout << (dq.empty() ? -1 : dq.front()) << '\n'; break;
		case 8: cout << (dq.empty() ? -1 : dq.back()) << '\n'; break;
		}
	}
}