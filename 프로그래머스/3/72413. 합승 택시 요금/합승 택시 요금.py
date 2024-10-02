def solution(n, s, a, b, fares):    
    matrix = [[1000001] * (n+1) for _ in range(n+1)]
    for i, j, cost in fares:
        matrix[i][j] = cost
        matrix[j][i] = cost
    
    for i in range(n+1):
        matrix[i][i] = 0
        
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if matrix[i][j] > matrix[i][k] + matrix[j][k]:
                    matrix[i][j] = matrix[i][k] + matrix[j][k]
        
    answer = 100000001
    for i in range(1, n+1):
        answer = min(answer, matrix[i][s] + matrix[i][a] + matrix[i][b])
        
    return answer