#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);

    int n;
    cin >> n;
    vector<pair<int, int>> dots(n);

    for (int i = 0; i < n; ++i) {
        cin >> dots[i].first >> dots[i].second;
    }

    int max_collinear = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int collinear = 0;
            for (int k = 0; k < n; ++k) {
                if ((dots[k].first - dots[i].first) * (dots[j].second - dots[i].second) ==
                    (dots[k].second - dots[i].second) * (dots[j].first - dots[i].first)) {
                    collinear++;
                }
            }
            max_collinear = max(max_collinear, collinear);
        }
    }

    if (max_collinear <= (2 * n) / 3) {
        cout << n / 3 << endl;
    } else {
        cout << n - max_collinear << endl;
    }

    return 0;
}
