#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;
int main() {
	string N; cin >> N; sort(N.begin(), N.end(), greater<>()); cout << N;
}