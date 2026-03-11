#include <iostream>
using namespace std;
void hanoi(int n, int s, int e) {
	if (n == 1) cout << s << ' ' << e << '\n';
	else { hanoi(n - 1, s, 6 - s - e); cout << s << ' ' << e << '\n'; hanoi(n - 1, 6 - s - e, e); }
}
int main() {
	int n; cin >> n; cout << (1 << n) - 1 << '\n'; hanoi(n, 1, 3);
}