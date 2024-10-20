#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int lower_bound(const vector<pair<int, int>>& array, int target) {
    int l = -1, r = array.size();
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (array[m].second < target) {
            l = m;
        } else {
            r = m;
        }
    }
    return r;
}

int upper_bound(const vector<pair<int, int>>& array, int target) {
    int l = -1, r = array.size();
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (array[m].second <= target) {
            l = m;
        } else {
            r = m;
        }
    }
    return r;
}

bool bin_search(const vector<pair<int, int>>& array, int lb, int ub, int left, int right, int target) {
    int l = lb - 1, r = ub;
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (array[m].first < left) {
            l = m;
        } else {
            r = m;
        }
    }
    return r < array.size() && array[r].second == target && left <= array[r].first && array[r].first <= right;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int n;
    cin >> n;
    vector<int> values(n);
    for (int i = 0; i < n; ++i) {
        cin >> values[i];
    }

    vector<pair<int, int>> array(n);
    for (int i = 0; i < n; ++i) {
        array[i] = {i + 1, values[i]};
    }

    stable_sort(array.begin(), array.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });

    int q;
    cin >> q;
    for (int i = 0; i < q; ++i) {
        int l, r, x;
        cin >> l >> r >> x;
        if (bin_search(array, lower_bound(array, x), upper_bound(array, x), l, r, x)) {
            cout << 1;
        } else {
            cout << 0;
        }
    }
    cout << endl;

    return 0;
}
