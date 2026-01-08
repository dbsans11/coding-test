#include <iostream>
using namespace std;
int main() {
	int N, r = 0; cin >> N;
	for (int i = 1; i < N; ++i) {
		int a = i, b = i; while (a) { b += a % 10; a /= 10; }
		if (b == N) { r = i; break; }
	} cout << r;
}