from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

def is_corner(before, current):
    if before == -1:
        return False
    if before in (0, 3) and current in (0, 3):
        return False
    if before in (1, 2) and current in (1, 2):
        return False
    return True

    

def solution(board):
    row_len, col_len = len(board), len(board[0])
    visited = dict()
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    answer = 1000000000
    def dfs(row, col, cost, before):
        if row == row_len - 1 and col == col_len - 1:
            nonlocal answer
            if answer > cost:
                answer = cost
            return
        for i in range(4):
            delta_row, delta_col = delta[i]
            next_row = row + delta_row
            next_col = col + delta_col
            if 0 <= next_row < row_len and 0 <= next_col < col_len:
                if board[next_row][next_col] == 1:
                    continue
                key = (next_row, next_col, i)
                if is_corner(before, i):
                    next_cost = cost + 600
                else:
                    next_cost = cost + 100
                if key not in visited or visited[key] > next_cost:
                    visited[key] = next_cost
                    dfs(next_row, next_col, next_cost, i)
    dfs(0, 0, 0, -1)
    return answer