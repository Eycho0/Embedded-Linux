#include <iostream>
#include <numeric>  

int main() {
    const int size = 10000;
    int arr[size];

    std::iota(arr, arr + size, 10);
    int sum = std::accumulate(arr,arr+size,0);

    std::cout << sum ;

}
