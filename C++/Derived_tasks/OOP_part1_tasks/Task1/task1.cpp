#include <algorithm>
#include <cstring>
#include <iostream>
#include <math.h>

class string
{
    private:
        char* strng;
        int len;
    public:
        string(char* str)
        {
            len = strlen(str);
            strng = new char[len+1];
            std::strcpy(strng,str);
        }

        int size()
        {
            return len;
        }

        void print()
        {
            std::cout<<strng;
        }

        ~string()
        {
            delete strng;
        }    
};

int main()
{
    string s("hello, world");

    int x = s.size();
    std::cout<<x<<std::endl;
    s.print();
    
}
