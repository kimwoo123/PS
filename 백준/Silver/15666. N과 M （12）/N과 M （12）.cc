#include <stdio.h>
#include <algorithm>

int N, M;
int answer[100];
int numbers[100];

void backtrack(int index, int count) {
    if (count == M) {
        for (int i = 0; i < M; ++i) 
            printf("%d ", answer[i]);
        printf("\n");
        return;
    }

    int before = 0;
    for (int i = index; i < N; ++i) {
        if (numbers[i] != before) {
            answer[count] = numbers[i];
            before = answer[count];
            backtrack(i, count + 1);
        }
    }
}

void input_data(void) {
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; ++i) {
        scanf("%d", &numbers[i]);
    }
}

int main(void) {
    input_data();
    std::sort(numbers, numbers+N);
    backtrack(0, 0);
}