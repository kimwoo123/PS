#include <stdio.h>
#include <algorithm>

int N, K;
int weights[100], values[100];
int dp[101][100001];

void solve(void) {
    int w, v;
    for (int i = 1; i < N+1; ++i){
        w = weights[i-1];
        v = values[i-1];
        for (int j = 1; j < K+1; ++j) {
            if (j < w)
                dp[i][j] = dp[i-1][j];
            else
                dp[i][j] = std::max(dp[i-1][j], v + dp[i-1][j-w]);
        }
    }
    printf("%d", dp[N][K]);
}

void input_data(void) {
    scanf("%d %d", &N, &K);

    int v, w;
    for (int i = 0; i < N; ++i) {
        scanf("%d %d", &w, &v);
        weights[i] = w;
        values[i] = v;
    }
}

int main(void) {
    input_data();
    solve();
}