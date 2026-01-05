#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int t[3]; cin >> t[0] >> t[1] >> t[2]; sort(t, t + 3); cout << (t[2] >= t[0] + t[1] ? 2 * (t[0] + t[1]) - 1 : t[0] + t[1] + t[2]);
}