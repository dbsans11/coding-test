#include <iostream>
using namespace std;
int main() {
	int N, M, r = 65; cin >> N >> M; char** a = new char* [N];
	for (int i = 0; i < N; ++i) { a[i] = new char[M]; for (int j = 0; j < M; ++j) cin >> a[i][j]; }
	char w[8][8] = { {'W','B','W','B','W','B','W','B'}, {'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'}, {'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'}, {'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'}, {'B','W','B','W','B','W','B','W'} };
	char b[8][8] = { {'B','W','B','W','B','W','B','W'}, {'W','B','W','B','W','B','W','B'},
		{'B','W','B','W','B','W','B','W'}, {'W','B','W','B','W','B','W','B'},
		{'B','W','B','W','B','W','B','W'}, {'W','B','W','B','W','B','W','B'},
		{'B','W','B','W','B','W','B','W'}, {'W','B','W','B','W','B','W','B'}, };
	for (int i = 0; i < N - 7; ++i) {
		for (int j = 0; j < M - 7; ++j) {
			int t = 0; for (int x = 0; x < 8; ++x) {
				for (int y = 0; y < 8; ++y) {
					t += !(a[i + x][j + y] == w[x][y]);
				}
			} r = t < r ? t : r;
			t = 0; for (int x = 0; x < 8; ++x) {
				for (int y = 0; y < 8; ++y) {
					t += !(a[i + x][j + y] == b[x][y]);
				}
			} r = t < r ? t : r;
		}
	} cout << r;
}