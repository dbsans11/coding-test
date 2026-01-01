#include <iostream>
using namespace std;
int main() {
	int N; cin >> N;
	int maximum = -1000001, minimum = 1000001;
	while (N--) { 
		int temp; cin >> temp;
		maximum = temp > maximum ? temp : maximum;
		minimum = temp < minimum ? temp : minimum;
	}
	cout << minimum << ' ' << maximum;
}