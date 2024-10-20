#include <iostream>
#include <cmath>

int area(int a, int b, int c) {
    return 2 * (a * b + a * c + b * c);
}

int main() {
    int n, k, ar;
    std::cin >> n;
    int a = 1, b = 1, c = n;
    int max_ar = area(a, b, c);

    for (int i = 1; i <= (int) ceil(pow(n, 1/3.0)); i++) {
        for (int j = 1; j <= (int) ceil(pow(n, 1/2.0)); j++) {
            k = n / (i * j);
            ar = area(i, j, k);
            if (n % (i * j) == 0 && ar < max_ar) {
                a = i;
                b = j;
                c = k;
                max_ar = ar;
            }
        }
    }

    std::cout << a << " " << b << " " << c << std::endl;
}
