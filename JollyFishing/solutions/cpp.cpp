#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    double mf, grow, fish;
    cin >> mf >> grow >> fish;
    grow = 1 + grow / 1000;
    fish = 1 - fish / 1000;

    double best = 0;
    for (int i = 1; i <= 365; i++) {
        double remaining = pow(grow, i) * pow(fish, (365-i));
        if (remaining >= 1)
            best = max(best, (pow(grow, i) - remaining) * mf);
    }
    cout << std::fixed << best << endl;
}
