#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; ++i)
		cin >> arr[i];

    int dp[n];
    int answer = 0;
    for (int i = 0; i < n; ++i) {
        dp[i] = 1;
        for (int j = 0; j < i; ++j) {
            if (arr[i] > arr[j])
                dp[i] = max(dp[i], dp[j] + 1);
        }
        answer = max(answer, dp[i]);
    }

    printf("%d", answer);
}