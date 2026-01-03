#include <iostream>
using namespace std;
int main() {
	int N; cin >> N; int cnt = N;
	while (N--) {
		int T; cin >> T;
		if (T == 1) --cnt;
		for (int i = 2; i*i <= T; ++i) {
			if (T % i == 0) { --cnt; break; }
		}
	} cout << cnt;
}