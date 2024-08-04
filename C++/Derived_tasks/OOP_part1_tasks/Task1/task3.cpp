#include <iostream>

int &fun() {
  static int x;
  std::cout << " x is currently " << x << std::endl;
  return x;
}

int main() {
  fun();
  fun() = 15;
  fun();
}
