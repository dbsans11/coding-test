#include <iostream>
using namespace std;
int gcd(int a, int b) { while (b != 0) { int r = a % b; a = b; b = r; } return a; }
int main() {
	int n; cin >> n; int* a = new int[n], * b = new int[n - 1]; for (int i = 0; i < n; ++i) cin >> a[i];
	for (int i = 0; i < n - 1; ++i) b[i] = a[i + 1] - a[i];
	int temp = gcd(b[1], b[0]), r = 0; for (int i = 2; i < n - 1; ++i) temp = gcd(b[i], temp);
	for (int i = 0; i < n - 1; ++i) r += (b[i] / temp - 1); cout << r;
}