#include <iostream>
#include <math.h>


int main()
{
    int a,b,c;
    std::cin >> a >> b >> c;

    a = std::pow(a,2);
    b = std::pow(b,2);
    c = std::pow(c,2);

    if(c == a+b || a == b+c || b == c+a)
        std::cout<<"Right";
    else
        std::cout << "Not right";
            
}
