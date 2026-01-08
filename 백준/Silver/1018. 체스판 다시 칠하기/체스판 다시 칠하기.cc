#include <iostream>
using namespace std;
int main() {
	int N, M, r = 65; cin >> N >> M; char** a = new char* [N];
	for (int i = 0; i < N; ++i) { a[i] = new char[M]; for (int j = 0; j < M; ++j) cin >> a[i][j]; }
	
	for (int i = 0; i < N - 7; ++i) {
		for (int j = 0; j < M - 7; ++j) {
			int w = 0, b = 0; for (int x = 0; x < 8; ++x) {
				for (int y = 0; y < 8; ++y) {
					if ((x + y) % 2 == 0) { if (a[i + x][j + y] != 'W') ++w; else ++b; }
					else { if (a[i + x][j + y] != 'B') ++w; else ++b; }
				}
			} r = w < r ? w : r; r = b < r ? b : r;
		}
	} cout << r;
}