#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
	string croatia[] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
	string T; cin >> T;
	for (string s : croatia) {
		while (T.find(s) != string::npos) {
			T.replace(T.find(s), s.length(), "*");
		}
	} cout << T.length();
}