#include <iostream>
#include <string>
using namespace std;
int main() {
	int N; cin >> N; int cnt = N;
	while (N--) {
		string T; int idx = 0; bool check[26] = { 0, }; cin >> T;
		for (int c : T) {
			if (check[c - 'a'] == 0 || idx == c - 'a') {
				idx = c - 'a'; check[idx] = 1;
			}
			else { --cnt; break; }
		}
	} cout << cnt;
}