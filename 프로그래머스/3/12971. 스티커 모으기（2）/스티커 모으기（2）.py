def solution(sticker):
    answer = 0
    l = len(sticker)
    if l == 1:
        return sticker[0]
    dp = [0] * l
    dp[1] = sticker[1]
    for i in range(2, l):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
        
    dp[0] = sticker[0]
    dp[1] = max(dp[0], dp[1])
    for i in range(2, l - 1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])

    return max(dp[-1], dp[-2])