#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
    
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    
    long long total = 0;
    
    for (int i = 0; i < n; ++i) {
        int window_end = min(i + 21, n);
        unordered_map<int, deque<int>> right;
        
        for (int j = i; j < window_end; ++j) {
            int val = arr[j];
            right[val].push_back(j);
        }
        
        int min_right = window_end;
        unordered_set<int> left;
        
        for (int mid = i; mid < window_end; ++mid) {
            int val = arr[mid];
            
            if (!right[val].empty()) {
                right[val].pop_front();
            }

            for (int diam = -5; diam <= 5; ++diam) {
                int target_left = val - diam;
                
                if (left.find(target_left) != left.end()) {
                    int target_right = val + diam;
                    auto it = right.find(target_right);
                    if (it != right.end() && !it->second.empty()) {
                        int candidate = it->second.front();
                        if (candidate < min_right) {
                            min_right = candidate;
                        }
                    }
                }
            }

            left.insert(val);
        }

        total += (n - min_right);
    }
    
    cout << total << endl;
    
    return 0;
}
