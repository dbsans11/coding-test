#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
	int M, N; cin >> M >> N;
	int sum = 0, min = 0;
	for (int i = N; i >= M; i--) {
		int j = 2;
		for (; j <= sqrt(i); j++) {
			if (i % j == 0) break;
		}
		if (i!=1 && j > sqrt(i)) sum += (min = i);
	}
	if (min == 0) cout << -1 << endl;
	else cout << sum << endl << min << endl;
}