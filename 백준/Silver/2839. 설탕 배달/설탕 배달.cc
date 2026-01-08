#include <iostream>
using namespace std;
int main() {
	int N, r = -1; cin >> N;
	for (int i = N / 5; i >= 0; --i) {
		int t = N - i * 5; if (t % 3 == 0) { r = i + t / 3; break; }
	} cout << r;
}