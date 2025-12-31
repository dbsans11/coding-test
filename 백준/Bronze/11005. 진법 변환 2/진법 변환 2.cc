#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
	int N, B; char temp; string res;
	cin >> N >> B;
	while (N) {
		if (N % B >= 0 && N % B <= 9) {
			temp = (N % B) + '0';
		}
		else {
			temp = ((N % B) - 10) + 'A';
		}
		res.push_back(temp);
		N /= B;
	}
	reverse(res.begin(), res.end());
	cout << res << endl;
	return 0;
}