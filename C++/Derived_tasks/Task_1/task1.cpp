#include <iostream>
#include <math.h>

void max(int* arr, int s)
{
    int m = INT_MIN;
    for (int i=0 ; i<s ; i++)
    {
        if (arr[i]>m)
        {
            m=arr[i];
        }
    }
    std::cout<<m;
}

int main()
{
    int arr[] = {1,2,3,4,5,6,7,9};
    int s =sizeof(arr)/sizeof(arr[0]);
    max(arr,s);
}
