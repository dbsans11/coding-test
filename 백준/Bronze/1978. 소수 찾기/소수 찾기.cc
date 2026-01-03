#include <iostream>
using namespace std;

int main(void)
{
	int n, sum=0; cin >> n;
	while (n--) {
		int tmp, i=2; cin >> tmp;
		for (; i < tmp; i++) {
			if (tmp % i == 0) break;
		}
		if (i == tmp) sum++;
	}
	cout << sum << endl;

	return 0;
}