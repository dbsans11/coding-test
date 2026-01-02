#include <iostream>
using namespace std;
int main(void)
{
	int paper[100][100] = { 0, };
	int n, x, y, cnt=0; cin >> n;
	while (n--) {
		cin >> x >> y;
		for (int q = y; q < y + 10; q++) {
			for (int p = x; p < x + 10; p++) {
				if (!paper[q][p]) {
					paper[q][p] = 1; cnt++;
				}
			}
		}
	}
	cout << cnt << endl;
	return 0;
}