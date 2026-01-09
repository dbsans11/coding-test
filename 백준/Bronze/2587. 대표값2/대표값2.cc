#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int a[5], t = 0; for (int i = 0; i < 5; ++i) { cin >> a[i]; t += a[i]; }
	sort(a, a + 5); cout << t / 5 << '\n' << a[2];
}