#include <iostream>
using namespace std;
int main() {
    int a = 5;
    int b = 6;
    int c = 7;

    int temp;
    temp = a;
    a = b;
    b = temp;
    
    temp = a;
    a = c;
    c = temp;

    cout << a << endl << b << endl << c;

    return 0;
}