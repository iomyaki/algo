#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

#define int long long

const int mod = 998244353;

struct Mint {
    int z;
    Mint() : z(0) {}
    Mint(int _z) : z(_z) {}
    Mint binpow(Mint a, int n) {
        Mint res(1);
        while (n) {
            if (n & 1) {
                res = res * a;
            }
            a = a * a;
            n /= 2;
        }
        return res;
    }
    Mint operator-(const Mint& other) const {
        int val = z - other.z + mod;
        if (val >= mod) { val -= mod; }
        return Mint(val);
    }
    Mint operator-(const int& other) const {
        int val = z - other + mod;
        if (val >= mod) { val -= mod; }
        return Mint(val);
    }
    Mint operator+(const Mint& other) const {
        int val = z + other.z;
        if (val >= mod) { val -= mod; }
        return Mint(val);
    }
    Mint operator+(const int& other) const {
        int val = z + other;
        if (val >= mod) { val -= mod; }
        return Mint(val);
    }
    Mint operator*(const Mint& other) const {
        int val = (1ll * z * other.z) % mod;
        return Mint(val);
    }
    Mint operator*(const int& other) const {
        int val = (1ll * z * other) % mod;
        return Mint(val);
    }
    Mint operator/(const Mint& other) const {
        return Mint(z) * Mint().binpow(other, mod - 2);
    }
};

Mint solvePrime(int n, vector<int>& deg, int p) {
    int sm = 0;
    for (const int& it : deg) {
        sm += it;
    }
    if (sm == 0) {
        return Mint(1);
    }

    vector<Mint> pow_p(sm + 1, 1);
    for (int i = 1; i <= sm; ++i) {
        pow_p[i] = pow_p[i - 1] * p;
    }
    vector<Mint> dp0(sm + 1), dp1(sm + 1);
    for (int i = 1; i <= sm; ++i) {
        dp0[i] = pow_p[i];
    }
    dp1[0] = 1;

    for (const int& diff : deg) {
        vector<Mint> new_dp0(sm + 1), new_dp1(sm + 1);
        for (int i = 0; i <= sm; ++i) {
            if (dp0[i].z == 0 && dp1[i].z == 0) {
                continue;
            }
            auto relax = [&](int upd_ind, Mint val0, Mint val1) {
                Mint w = pow_p[upd_ind];
                if (val0.z != 0) {
                    if (upd_ind == 0) {
                        new_dp1[upd_ind] = new_dp1[upd_ind] + w * val0;
                    } else {
                        new_dp0[upd_ind] = new_dp0[upd_ind] + w * val0;
                    }
                }
                if (val1.z != 0) {
                    new_dp1[upd_ind] = new_dp1[upd_ind] + w * val1;
                }
            };

            if (diff == 0) {
                relax(i, dp0[i], dp1[i]);
            } else {
                if (i >= diff) {
                    relax(i - diff, dp0[i], dp1[i]);
                }
                if (i + diff <= sm) {
                    relax(i + diff, dp0[i], dp1[i]);
                }
            }
        }
        dp0.swap(new_dp0);
        dp1.swap(new_dp1);
    }
    Mint res = 0;
    for (Mint it : dp1) {
        res = res + it;
    }
    return res;
}

signed main() {
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);

    int n;
    cin >> n;
    vector<int> a(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        cin >> a[i];
    }

    vector<int> primes;
    for (int i = 2; i <= 1000; ++i) {
        bool ok = true;
        for (int j = 2; j * j <= i; ++j) {
            if (i % j == 0) {
                ok = false;
                break;
            }
        }
        if (ok) {
            primes.emplace_back(i);
        }
    }

    unordered_map<int, vector<int>> deg_primes;
    for (int p : primes) {
        deg_primes[p] = vector<int>(n - 1, 0);
    }
    for (int i = 0; i < n - 1; ++i) {
        int x = a[i];
        for (int p : primes) {
            if (p * p > x) break;
            int cnt = 0;
            while (x % p == 0) {
                x /= p;
                ++cnt;
            }
            deg_primes[p][i] = cnt;
        }
        if (x > 1) {
            if (!deg_primes.count(x)) {
                deg_primes[x] = vector<int>(n - 1, 0);
            }
            deg_primes[x][i] = 1;
        }
    }

    Mint ans(1);
    for (auto& fctr : deg_primes) {
        bool it_has = false;
        for (int& it : fctr.second) {
            if (it != 0) {
                it_has = true;
                break;
            }
        }
        if (it_has) {
            ans = ans * solvePrime(n, fctr.second, fctr.first);
        }
    }
    
    cout << ans.z << endl;
    
    return 0;
}
