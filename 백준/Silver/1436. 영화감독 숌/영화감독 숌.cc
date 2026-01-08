#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
	int N, i = 0, a = 665; cin >> N;
	while (i < N) {
		++a; string b = to_string(a);
		if (b.find("666") != string::npos) ++i;
	} cout << a;
}