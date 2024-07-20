#include <iostream>

int main()
{
    std::string str = "aeiouAEIOU";
    char a;
    std::cin >> a;
    for(char c : str)
    {
        if(c == a)
        {
            std::cout << "vowel";
            return 0;
        }
    }
    std::cout<<"not vowel";

}
