#include <iostream>
#include <algorithm>
#include <limits>
#include <vector>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b) {
    while (b > 0) {
        a = a % b;
        swap(a, b);
    }
    return a;
}

ll lcm(ll a, ll b) {
    return (a / gcd(a, b)) * b;
}

ll to_add(ll num, ll mod) {
    return (mod - (num % mod)) % mod;
}

int main() {
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);

    int n;
    ll x, y, z;
    cin >> n >> x >> y >> z;
    
    vector<ll> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    ll lcm_xy = lcm(x, y);
    ll lcm_xz = lcm(x, z);
    ll lcm_yz = lcm(y, z);
    ll lcm_xyz = lcm(lcm_xy, z);
    
    vector<vector<ll>> minim(n, vector<ll>(8, numeric_limits<ll>::max()));
    for (int i = 0; i < n; i++) {
        ll num = arr[i];
        minim[i][1] = to_add(num, x);
        minim[i][2] = to_add(num, y);
        minim[i][4] = to_add(num, z);
        minim[i][3] = to_add(num, lcm_xy);
        minim[i][5] = to_add(num, lcm_xz);
        minim[i][6] = to_add(num, lcm_yz);
        minim[i][7] = to_add(num, lcm_xyz);
    }
    
    for (int i = 1; i < n; i++) {
        vector<ll> new_minim(8, numeric_limits<ll>::max());
        for (int m1 = 1; m1 < 8; m1++) {
            new_minim[m1] = min(minim[i][m1], minim[i - 1][m1]);
        }
        for (int m2 = 1; m2 < 8; m2++) {
            for (int m3 = 1; m3 < 8; m3++) {
                int m4 = m2 | m3;
                new_minim[m4] = min(new_minim[m4], minim[i][m3] + minim[i - 1][m2]);
            }
        }
        minim[i] = new_minim;
    }
    
    cout << minim[n - 1][7] << endl;
    return 0;
}
