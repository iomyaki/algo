#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

class Item {
public:
  Item() {
    index = 0;
    value = 0;
    weight = 0;
  }
  Item(long long idx, long long val, long long w) {
    index = idx;
    value = val;
    weight = w;
  }
    long long index;
    long long value;
    long long weight;
};



bool chooseK(const vector<Item>& items, int k, double ratio, vector<int>& selectedIndices) {
    vector<pair<double, int>> weightedIndexes;

    for (const auto &item : items) {
        pair<double, int> temp = {static_cast<double>(item.value) - ratio * item.weight, item.index};
        weightedIndexes.push_back(temp);
    }
    sort(weightedIndexes.rbegin(), weightedIndexes.rend());
    double sum = 0;
    selectedIndices.clear();

    for (int i = 0; i < k; ++i) {
        sum += weightedIndexes[i].first;
        selectedIndices.push_back(weightedIndexes[i].second);

        if (sum < 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<Item> items;
    for (int i = 0; i < n; ++i) {
        int value, weight;
        cin >> value >> weight;
        Item temp(i + 1, value, weight);
        items.push_back(temp);
    }

    double low = -1, high = 1e6+1;
    double bestRatio = 0.0;
    vector<int> indices;

    while (high - low > 1e-9) {
        double mid = (low + high) / 2;

        vector<int> selectedIndices;
        if (chooseK(items, k, mid, selectedIndices)) {
            bestRatio = mid;
            low = mid;
            indices = selectedIndices;
        } else {
            high = mid;
        }
    }

    for (int idx : indices) {
        cout << idx << " ";
    }
    cout << endl;

    return 0;
}
