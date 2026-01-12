#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool cmp(string s1, string s2) { if (s1.length() == s2.length()) return s1 < s2; else return s1.length() < s2.length(); }
int main() {
	int N; cin >> N; string* a = new string[N]; for (int i = 0; i < N; ++i) cin >> a[i];
	sort(a, a + N, cmp); 
	for (int i = 0; i < N; ++i) if (i == 0 || a[i] != a[i - 1]) cout << a[i] << '\n';
}