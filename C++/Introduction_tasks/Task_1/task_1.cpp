#include <iostream>

int main()
{
    std::cout << "+---------+--------+" << std::endl;
    std::cout << "| char   |  ASCII  |" << std::endl;
    std::cout << "+---------+--------+" << std::endl;

    int a = 0;
    while (a<256)
    {
        std::cout << "|  ";
        if(isalnum(a))
        {
            std::cout << char(a) << "    |   " << a << "  |"  << std::endl; 
        }
        else
        {
            std::cout << "     |   " << a << "  |"  << std::endl; 

        }
        a++;
    }
    
}
