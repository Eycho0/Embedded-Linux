#include <iostream>
#include <math.h>

int main()
{
    int arr1[] = {1,2,3,4};
    int arr2[] = {5,6,7,8};
    
    int s1 = sizeof(arr1)/sizeof(int);
    int s2 = sizeof(arr2)/sizeof(int);
    int s =s1+s2;
    int arr[s];

    for (int i = 0; i < s1; ++i) {
        arr[i] = arr1[i];
    }

    for (int i = 0; i < s2; ++i) {
        arr[s1 + i] = arr2[i];
    }

    for (int i = 0; i < s; ++i) {
        std::cout << arr[i] << ' ';
    }
    
}
