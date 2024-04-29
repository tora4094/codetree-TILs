#include <iostream>
using namespace std;
int main() {
    double n;
    double ftToCm = 30.48;
    cin >> n;
    cout << fixed;
    cout.precision(1);
    cout << n * ftToCm;
    return 0;
}