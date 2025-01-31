#include <iostream>
#include <algorithm>
#include <tuple>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);

    int n, k;
    cin >> n >> k;

    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    vector<long long> numb_pow(n, 1);
    vector<long long> sum_p(301);
    sum_p[0] = n;

    for (int power = 1; power <= 300; ++power) {
        long long current_sum = 0;
        for (int i = 0; i < n; ++i) {
            numb_pow[i] = numb_pow[i] * numbers[i] % MOD;
            current_sum = (current_sum + numb_pow[i]) % MOD;
        }
        sum_p[power] = current_sum;
    }

    vector<vector<long long>> binom(301, vector<long long>(301));
    binom[0][0] = 1;
    for (int power = 1; power <= 300; ++power) {
        binom[power][0] = 1;
        binom[power][power] = 1;
        for (int i = 1; i < power; ++i) {
            binom[power][i] = (binom[power - 1][i] + binom[power - 1][i - 1]) % MOD;
        }
    }

    long long denominator = (MOD + 1) >> 1;
    for (int power = 1; power <= k; ++power) {
        long long result = 0;
        for (int i = 0; i <= power; ++i) {
            long long factor = ((sum_p[i] * sum_p[power - i] % MOD - sum_p[power] + MOD) % MOD) * binom[power][i] % MOD;
            factor = factor * denominator % MOD;
            result = (result + factor) % MOD;
        }
        cout << result << endl;
    }

    return 0;
}
