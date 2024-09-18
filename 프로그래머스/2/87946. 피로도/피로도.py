def solution(k, dungeons):
    answer = 0
    l = len(dungeons)
    visited = [0] * l
    def dfs(count, tired):
        nonlocal answer
        if answer < count:
            answer = count
        for i in range(l):
            if dungeons[i][0] <= tired and visited[i] == 0:
                visited[i] = 1
                dfs(count + 1, tired - dungeons[i][1])
                visited[i] = 0
    dfs(0, k)
    return answer