#include <iostream>
#include <math.h>

int main()
{
    int arr[] = {1,2,3,4,7,9,10,14,15};
    
    int s = sizeof(arr)/sizeof(int);
    int even=0,odd=0;

    for(int i=0 ; i<s ;i++)
    {
        if(arr[i]&1)
        {
            odd++;
        }
        else
            even++;
    }
    std::cout<<even<<' '<<odd;
    
}
