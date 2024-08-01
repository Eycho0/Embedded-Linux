#include <iostream>
#include <math.h>

int b_s(int* arr, int start , int end , int search)
{
    auto cnt=0;
    while(start<=end)
    {
        cnt++;
        int mid  = (start + end)/2;

        if(arr[mid] == search)
        {
            return arr[mid];
        }

        else if(arr[mid]>search)
        {
            end = mid-1;
        }

        else if (arr[mid]<search)
        {
            start = mid+1;
        }

    }
    std::cout<<cnt<<'\n';
    return -1;
}

int main()
{
    int arr[] = {1,2,3,4,5,6,7,9};
    int s =sizeof(arr)/sizeof(arr[0]);
    int search;
    std::cin>> search;
    int x = b_s(arr , 0,s,search);
    std::cout<<x;
}
