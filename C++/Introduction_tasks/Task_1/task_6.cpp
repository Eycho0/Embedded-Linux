#include <iostream>

int main()
{
    int a;
    std::cin >> a;

    int sum=0;
    while(a>0)
    {
        sum += a%10;
        a/=10;
    }
    std::cout << sum;
}
