#include <iostream>
using namespace std;
long long fact(int n) { return ((n == 0 || n == 1 ? 1 : (long long)fact(n - 1) * n)); }
int main() { int n; cin >> n; cout << fact(n); }