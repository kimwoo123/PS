#include <stdio.h>
#include <algorithm>

int N, M;
int answer[100];
int numbers[100];
bool visited[100] = { false };

void backtrack(int count) {
    if (count == M) {
        for (int i = 0; i < M; ++i) 
            printf("%d ", answer[i]);
        printf("\n");
        return;
    }

    int before = 0;
    for (int i = 0; i < N; ++i) {
        if (!visited[i] && numbers[i] != before) {
            answer[count] = numbers[i];
            before = answer[count];
            visited[i] = true;
            backtrack(count + 1);
            visited[i] = false;
        }
    }
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; ++i) {
        scanf("%d", &numbers[i]);
    }

    std::sort(numbers, numbers+N);
    backtrack(0);
}