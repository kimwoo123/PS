def solution(land):
    answer = 0

    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    
    for i in range(N):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][k] for k in range(4) if j != k)
            
    return max(dp[-1])