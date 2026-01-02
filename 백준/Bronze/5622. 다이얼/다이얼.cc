#include <iostream>
#include <string>
using namespace std;
int main() {
	string num_pad[8] = { "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ" };
	string T; cin >> T; int n = 0;
	for (char c : T) {
		for (int i = 0; i < 8; i++) {
			if (num_pad[i].find(c) != string::npos)
				n += 3 + i;
		}
	} cout << n;
}