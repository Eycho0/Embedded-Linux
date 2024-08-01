#include <iostream>
#include <math.h>

void del(int* arr,int size, int index)
{
    for (int i = index ; i<size-1 ; i++)
    {
        arr[i] = arr[i+1];
    }
}

int main()
{
    int arr[] = {1,2,3,4,5,6,7,9};
    int s =sizeof(arr)/sizeof(arr[0]);
    del(arr,s,5);
    for(int i =0 ; i<s ; i++)
    {
        std::cout<<arr[i]<<' ';
    }
}
