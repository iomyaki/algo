#include <stdint.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

uint32_t a, b;
uint32_t cur = 0;

uint32_t nextRand24() {
    cur = cur * a + b;
    return cur >> 8;
}

uint32_t nextRand32() {
    uint32_t x = nextRand24(), y = nextRand24();
    return (x << 8) ^ y;
}

void insertion_sort(vector<uint32_t>& arr) {
    for (int i = 1; i < arr.size(); ++i) {
        uint32_t key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int t, n;
    cin >> t >> n;
    cin >> a >> b;

    vector<vector<uint32_t>> buckets(n);
    double const_value = static_cast<double>(n) / 4294967296.0;

    for (int _ = 0; _ < t; ++_) {
        int idx = 1;
        long long summ = 0;

        for (auto& bucket : buckets) {
            bucket.clear();
        }

        for (int i = 0; i < n; ++i) {
            uint32_t z = nextRand32();
            int bucket_idx = static_cast<int>(floor(const_value * z));
            buckets[bucket_idx].push_back(z);
        }

        for (auto& bucket : buckets) {
            insertion_sort(bucket);

            for (uint32_t x : bucket) {
                summ += static_cast<long long>(x) * idx;
                idx++;
            }
        }

        cout << summ << endl;
    }

    return 0;
}
