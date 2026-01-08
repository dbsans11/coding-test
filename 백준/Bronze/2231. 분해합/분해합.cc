#include <iostream>
using namespace std;

int main(void)
{
	int inp, cnt, sum; cin >> inp;
	for (int i = 1; i < inp; i++) {
		cnt = i; sum = i;
		while (cnt) { sum += cnt % 10; cnt /= 10; }
		if (inp == sum) { cout << i; return 0; }
	}
	cout << 0; 
	
	return 0;
}