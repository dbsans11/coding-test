#include <iostream>
using namespace std;

int main(void)
{
	int N; cin >> N;
	for (int i = 2; i <= N;i++) {
		while (!(N % i)) {
			cout << i << endl;
			N /= i;
		}
	}
}