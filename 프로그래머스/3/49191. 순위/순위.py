def solution(n, results):
    inf = 2
    matrix = [[inf] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        matrix[i][i] = 0
        
    for a, b in results:
        matrix[a][b] = 1
    
    answer = [0] * (n+1)
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if (matrix[i][k] == 1 and matrix[k][j] == 1):
                    matrix[i][j] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if matrix[i][j] == 1:
                answer[i] += 1
                answer[j] += 1
                
    count = 0
    for i in answer:
        if i == n - 1:
            count += 1
    
    return count