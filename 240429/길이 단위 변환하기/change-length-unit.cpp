#include <iostream>
using namespace std;
int main() {
    double a = 9.2;
    double b = 1.3;
    double ftToCm = 30.48;
    double miToCm = 160934; 

    cout << fixed;    
    cout.precision(1);
    cout << a << "ft = " << a * ftToCm << "cm" << endl;
    cout << b << "mi = " << b * miToCm << "cm" << endl;
    return 0;
}