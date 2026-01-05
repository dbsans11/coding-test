#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	while (true) {
		int a, b, c; cin >> a >> b >> c;
		if (a == 0) break;
		if (max({ a, b, c }) * 2 >= a + b + c) cout << "Invalid\n";
		else if (a == b && b == c) cout << "Equilateral\n";
		else if (a == b || b == c || c == a) cout << "Isosceles\n";
		else cout << "Scalene\n";
	}
}