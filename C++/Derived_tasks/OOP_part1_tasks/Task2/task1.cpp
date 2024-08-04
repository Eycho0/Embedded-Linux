#include <iostream>
#include <numeric>  

int main() {
    const int size = 10000;
    int arr[size];

    std::iota(arr, arr + size, 10);

    for (int i = 0; i < 10; ++i) {
        std::cout << arr[i] << " ";
    }

}
