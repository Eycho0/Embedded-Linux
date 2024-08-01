#include <iostream>
#include <math.h>


int main()
{
    int n =10;

    [&n](){
        n *= n;
    }();
    
    std::cout<<n;
}
