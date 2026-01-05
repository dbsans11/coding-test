#include <iostream>
using namespace std;
int main() {
	int n; cin >> n;
	int min_x = 10001, max_x = -10001, min_y = 10001, max_y = -10001;
	while (n--) {
		int tx, ty; cin >> tx >> ty;
		min_x = tx < min_x ? tx : min_x; max_x = tx > max_x ? tx : max_x;
		min_y = ty < min_y ? ty : min_y; max_y = ty > max_y ? ty : max_y;
	} cout << (max_x - min_x) * (max_y - min_y);
}