#include <iostream>
#include <cmath>
#include <deque>

using namespace std;

int main() {
    int n, k, temp, x, y, mod = pow(2, 30);
    cin >> n >> k;
    deque<int> numbers;

    for (int i = 0; i < n; i++) {
        cin >> temp;
        numbers.push_back(temp);
    }

    for (int i = 0; i < k; i++) {
        x = numbers.at(0);
        y = numbers.at(n - 1);
        if (x < y) {
            numbers.pop_front();
            numbers.push_back((x + y) % mod);
        }
        else {
            numbers.pop_back();
            numbers.push_front((y - x + mod) % mod);
        }
    }

    for (int num: numbers) {
        cout << num << " ";
    }
    cout << endl;
}
