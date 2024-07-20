#include <iostream>

int main()
{
    int a,b,c;
    std::cin >> a >> b >> c;
    int max;
    a>b? a>c? max=a : max = c : b>c? max=b : max=c;
    std::cout << max;        
}
