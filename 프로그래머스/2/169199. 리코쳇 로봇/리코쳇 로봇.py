from collections import deque

def solution(board):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def bfs(row_, col_, depth_):
        queue = deque([(row_, col_, depth_)])
        while queue:
            row, col, depth = queue.popleft()
            for delta_row, delta_col in delta:
                next_row, next_col = row, col
                while True:
                    next_row += delta_row
                    next_col += delta_col
                    if 0 <= next_row < row_len and 0 <= next_col < col_len:
                        if board[next_row][next_col] == 'D':
                            break
                    else:
                        break
                next_row -= delta_row
                next_col -= delta_col
                next_pos = (next_row, next_col)
                if next_pos not in visited or visited[next_pos] > depth:
                    visited[next_pos] = depth + 1
                    queue.append((next_row, next_col, depth + 1))
            
    row_len = len(board)
    col_len = len(board[0])
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == 'R':
                pos = (i, j)
            elif board[i][j] == 'G':
                dest = (i, j)
    
    visited = {pos: 0}
    bfs(pos[0], pos[1], 0)
    answer = visited.get(dest, -1)
    return answer