def solution(n, computers):
    row_len = len(computers)
    col_len = len(computers[0])
    visited = [0] * row_len
    
    count = 0
    for i in range(row_len):
        if visited[i] == 0:
            stack = [i]
            visited[i] = 1
            count += 1
            while stack:
                row = stack.pop()
                for j in range(col_len):
                    if computers[row][j] == 1 and visited[j] == 0:
                        visited[j] = 1
                        stack.append(j)
                    
    
    return count