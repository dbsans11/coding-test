#include <iostream>
#include <vector>
using namespace std;
int main() {
	while (true) {
		int n; cin >> n; if (n == -1) break;
		vector<int> arr; int sum = 0;
		for (int i = 1; i < n; ++i) { if (n % i == 0) { arr.push_back(i); sum += i; } }
		cout << n; if (sum == n) {
			cout << " = ";
			for (int i = 0; i < arr.size() - 1; ++i) cout << arr[i] << " + ";
			cout << arr[arr.size() - 1] << '\n';
		} else cout << " is NOT perfect.\n";
	}
}