#include <iostream>
#include <csignal>

void signalhandler(int signal)
{
    std::cout << "interrupt signal" << signal << " received"<<std::endl;
}

int main()
{
    std::cout << "program started \n";
    signal(SIGINT, signalhandler);

    while (1)
    {

    }
    
}
