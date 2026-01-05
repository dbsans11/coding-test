#include <iostream>
using namespace std;
int main() {
	int x1, y1, x2, y2, x3, y3; cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
	if (x1 != x2) cout << ((x1 != x3) ? x1 : x2) << ' '; else cout << x3 << ' ';
	if (y1 != y2) cout << ((y1 != y3) ? y1 : y2); else cout << y3;
}