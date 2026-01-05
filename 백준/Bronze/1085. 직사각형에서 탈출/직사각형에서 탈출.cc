#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int x, y, w, h; cin >> x >> y >> w >> h;
	w -= x; h -= y; cout << min({ x,y,w,h });
}