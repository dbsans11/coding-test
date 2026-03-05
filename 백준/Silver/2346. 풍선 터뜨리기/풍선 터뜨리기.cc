#include <iostream>
#include <deque>
using namespace std;
int main() {
	int n; cin >> n; deque<int> idx; for (int i = 1; i <= n; ++i) idx.push_back(i);
	deque<int> num; for (int i = 0; i < n; ++i) { int t; cin >> t; num.push_back(t); }
	while (1) {
		cout << idx.front() << ' '; idx.pop_front();
		int t = num.front(); num.pop_front();
		if (idx.empty()) break;
		if (t > 0) { 
			for (int i = 0; i < t - 1; ++i) {
				idx.push_back(idx.front()); idx.pop_front();
				num.push_back(num.front()); num.pop_front();
			}
		} else {
			for (int i = 0; i < -t; ++i) {
				idx.push_front(idx.back()); idx.pop_back();
				num.push_front(num.back()); num.pop_back();
			}
		}
	}
}