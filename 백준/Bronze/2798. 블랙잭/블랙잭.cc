#include <iostream>
using namespace std;
int main() {
	int N, M, r = 0; cin >> N >> M; int* arr = new int[N]; for (int i = 0; i < N; ++i) cin >> arr[i];
	for (int i = 0; i < N - 2; ++i) {
		for (int j = i + 1; j < N - 1; ++j) {
			for (int k = j + 1; k < N; ++k) { int t = arr[i] + arr[j] + arr[k]; r = t > r && t <= M ? t : r; }
		}
	} cout << r;
}