#include <stdio.h>

int N, M;
int matrix[100][100];

void solve(void) {
    for (int target = 0; target < N; ++target) {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (matrix[i][j] > matrix[i][target] + matrix[target][j]) {
                    matrix[i][j] = matrix[i][target] + matrix[target][j];
                }
            }
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (matrix[i][j] == 10000001)
                printf("%d ",0);
            else
                printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }
}

void input_data(void) {
    scanf("%d", &N);
    scanf("%d", &M);
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (i == j)
                matrix[i][j] = 0;
            else
                matrix[i][j] = 10000001;
        }
    }

    int a, b, c;
    for (int i = 0; i < M; ++i) {
        scanf("%d %d %d", &a, &b, &c);
        if (matrix[a-1][b-1] > c)
            matrix[a-1][b-1] = c;
    }
}

int main(void) {
    input_data();
    solve();
}