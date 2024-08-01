#include <algorithm>
#include <iostream>
#include <math.h>


int main()
{
    int arr[] = {1,3,5,7,9,4,3,1,2};
    int s = sizeof(arr)/sizeof(int);

    auto sort = [&]()->void{
        for(int i = 0 ; i < s ; i++)
        {
            for (int j = i+1 ; j < s ; j++)
            {
                if (arr[i] > arr[j])
                {
                    int tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                }
            }
        }
    };
    sort();
    for(auto& i : arr)
    {
        std::cout<<i<<' ';
    }
}
