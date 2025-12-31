#include <iostream>
#include <string>
using namespace std;
int main() {
	int N, B; cin >> N >> B;
	string res = "";
	while (N) {
		int temp = N % B;
		N /= B;
		res = (char)(temp >= 10 ? temp - 10 + 'A' : temp + '0') + res;
	}
	cout << res;
}