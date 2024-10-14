def solution(maps):
    row_len, col_len = len(maps), len(maps[0])
    
    visited = [[10000] * col_len for _ in range(row_len)]
    visited[0][0] = 1
    
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = [(0, 0, 1)]
    while queue:
        row, col, count = queue.pop(0)
        for delta_row, delta_col in delta:
            next_row = row + delta_row
            next_col = col + delta_col
            if 0 <= next_row < row_len and 0 <= next_col < col_len:
                if maps[next_row][next_col] and visited[next_row][next_col] > count + 1:
                    queue.append((next_row, next_col, count + 1))
                    visited[next_row][next_col] = count + 1
    
    if visited[-1][-1] == 10000:
        return -1
    return visited[-1][-1]