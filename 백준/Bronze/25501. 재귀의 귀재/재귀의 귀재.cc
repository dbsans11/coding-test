#include <iostream>
#include <string>
using namespace std;
int i;
int recursion(const string& s, int l, int r) {
	i++; if (l >= r) return 1; else if (s[l] != s[r])return 0; else return recursion(s, l + 1, r - 1);
}
int isPalindrome(const string& s) { return recursion(s, 0, s.length() - 1); }
int main() {
	ios::sync_with_stdio(0); cin.tie(NULL);
	int n; cin >> n; while (n--) {
		string s; i = 0; cin >> s; cout << isPalindrome(s) << ' ' << i << '\n';
	}
}