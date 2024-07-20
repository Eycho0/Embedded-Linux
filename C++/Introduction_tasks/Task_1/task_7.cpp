#include <bitset>
#include <iostream>
using namespace std;
int main()
{
    int num;
    cout << "enter a decimal number : ";
    cin >> num;
    bitset<8> x(num);
    cout << "binary representation : " <<  x << endl;
    
    string n;
    cout << "enter a binary number : ";
    cin >> n;
    bitset<8> y(n);
    cout << "decimal representation : " <<  y.to_ulong();
}
