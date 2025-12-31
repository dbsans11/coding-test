#include <iostream>
#include <string>
using namespace std;
int main() {
	string N; int B; cin >> N >> B;
	int res = 0;
	for (int i = 0; i < N.length(); ++i) {
		int temp = N[i];
		res = res * B + (temp <= '9' ? temp - '0' : temp - 'A' + 10);
	}
	cout << res;
}