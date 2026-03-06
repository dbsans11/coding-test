#include <iostream>
#include <deque>
using namespace std;
int main() {
	ios::sync_with_stdio(0); cin.tie(NULL);
	int n, m; cin >> n; bool* a = new bool[n]; for (int i = 0; i < n; ++i) cin >> a[i];
	deque<int> dq; for (int i = 0; i < n; ++i) { int b; cin >> b; if (!a[i]) dq.push_back(b); }
	cin >> m; for (int i = 0; i < m; ++i) {
		int c; cin >> c; dq.push_front(c); cout << dq.back() << ' '; dq.pop_back();
	}
}