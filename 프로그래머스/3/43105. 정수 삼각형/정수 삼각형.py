def solution(triangle):
    l = len(triangle)
    for i in range(1, l):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i-1][min(i-1, j)], triangle[i-1][max(0, j-1)])
    answer = max(triangle[-1])
    return answer