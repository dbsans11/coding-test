#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
int main() {
	int k; cin >> k; vector<int> v; 
	while (k--) { int n; cin >> n; if (n) v.push_back(n); else v.pop_back(); }
	cout << accumulate(v.begin(), v.end(), 0);
}