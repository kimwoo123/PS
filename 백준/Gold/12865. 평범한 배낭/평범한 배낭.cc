#include <stdio.h>
#include <algorithm>

int N, K;
int dp[100001];

void solve(void) {
    int w, v;
    for (int i = 0; i < N; ++i){
        scanf("%d %d", &w, &v);
        for (int j = K; j >= w; --j) {
            dp[j] = std::max(dp[j-w] + v, dp[j]);
        }
    }
    printf("%d", dp[K]);
}

void input_data(void) {
    scanf("%d %d", &N, &K);
}

int main(void) {
    input_data();
    solve();
}