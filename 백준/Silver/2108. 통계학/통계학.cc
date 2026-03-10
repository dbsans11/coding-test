#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int n, most_val = 0; double sum = 0; cin >> n; vector<int> v(n); vector<int> m(8001);
	for (int i = 0; i < n; ++i) { 
		cin >> v[i]; sum += v[i];
		most_val = ++m[v[i] + 4000] > most_val ? m[v[i] + 4000] : most_val;
	} sort(v.begin(), v.end()); 

	bool is_over = count(m.begin(), m.end(), most_val) > 1;
	auto most_idx = find(m.begin(), m.end(), most_val);
	if (is_over) most_idx = find(most_idx + 1, m.end(), most_val);
	
	cout << round(sum / n) + 0 << '\n' << v[(int)(n / 2)] << '\n' << most_idx - m.begin() - 4000 << '\n' << v[n - 1] - v[0];
}