#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	bool arr[100][100] = { 0, }; int T, cnt = 0; cin >> T;
	while (T--) {
		int x, y; cin >> x >> y;
		for (int i = x; i < x + 10; ++i) {
			for (int j = y; j < y + 10; ++j) {
				if (!arr[i][j]) { arr[i][j] = 1; ++cnt; }
			}
		}
	} cout << cnt;
}