#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, L, array[1000][1000], preproc[1000][1000], answer[1000][1000];
    cin >> n >> L;

    // read data
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> array[i][j];
        }
    }

    // perform preprocessing
    for (int i = 0; i < n; i++) {
        deque<int> window;
        deque<int> minimum;

        for (int j = 0; j < n; j++) {
            window.push_back(array[i][j]);

            while (minimum.size() > 0 and minimum.at(minimum.size() - 1) > array[i][j]) {
                minimum.pop_back();
            }
            minimum.push_back(array[i][j]);

            if (window.size() > L) {
                if (minimum.at(0) == window.at(0)) {
                    minimum.pop_front();
                }
                window.pop_front();
            }

            if (window.size() >= L) {
                preproc[i][j - L + 1] = minimum.at(0);
            }
        }
    }

    // slide through columns
    for (int j = 0; j < n - L + 1; j++) {
        deque<int> window;
        deque<int> minimum;

        for (int i = 0; i < n; i++) {
            window.push_back(preproc[i][j]);

            while (minimum.size() > 0 and minimum.at(minimum.size() - 1) > preproc[i][j]) {
                minimum.pop_back();
            }
            minimum.push_back(preproc[i][j]);

            if (window.size() > L) {
                if (minimum.at(0) == window.at(0)) {
                    minimum.pop_front();
                }
                window.pop_front();
            }

            if (window.size() >= L) {
                answer[j][i - L + 1] = minimum.at(0);
            }
        }
    }

    // print the answer
    for (int j = 0; j < n - L + 1; j++) {
        for (int i = 0; i < n - L + 1; i++) {
            cout << answer[i][j] << " ";
        }
        cout << endl;
    }
}
