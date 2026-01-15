#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	ios::sync_with_stdio(0); cin.tie(NULL);
	int a, b; cin >> a >> b; vector<int> A(a), B(b), v; 
	for (int i = 0; i < a; ++i) cin >> A[i]; for (int i = 0; i < b; ++i) cin >> B[i]; sort(A.begin(), A.end()); sort(B.begin(), B.end()); 
	set_symmetric_difference(A.begin(), A.end(), B.begin(), B.end(), back_inserter(v)); cout << v.size();
}