#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	int cnt[26] = { 0, }; string T; cin >> T;
	for (int c : T) ++cnt[c >= 'a' ? c - 'a' : c - 'A'];
	if (count(cnt, cnt + 26, *max_element(cnt, cnt + 26)) >= 2) cout << '?';
	else cout << (char)(max_element(cnt, cnt + 26) - cnt + 'A');
}