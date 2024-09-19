#include <iostream>
#include <cmath>

unsigned long long area(int a, int b, unsigned long long c) {
    return 2 * (a * b + a * c + b * c);
}

int main() {
    unsigned long long n, ar, k;
    std::cin >> n;
    int a = 1, b = 1;
    unsigned long long c = n, max_ar = area(a, b, c);

    for (int i = 1; i <= (int) ceil(pow(n, 1/3.0)); i++) {
        if (n % i == 0) {
            for (int j = i; j <= (int) ceil(pow(n / i, 1/2.0)); j++) {
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
    }

    std::cout << max_ar << " " << a << " " << b << " " << c << std::endl;
}
