def solution(maps):
    answer = []
    row_len = len(maps)
    col_len = len(maps[0])
    visited = [[0] * col_len for _ in range(row_len)]
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(row_len):
        for j in range(col_len):
            if maps[i][j] != "X" and visited[i][j] == 0:
                stack = [(i, j)]
                visited[i][j] = 1
                count = int(maps[i][j])
                while (stack):
                    row, col = stack.pop()
                    for delta_row, delta_col in delta:
                        next_row = row + delta_row
                        next_col = col + delta_col
                        if 0 <= next_row < row_len and 0 <= next_col < col_len:
                            if maps[next_row][next_col] != "X" and visited[next_row][next_col] == 0:
                                visited[next_row][next_col] = 1
                                stack.append((next_row, next_col))
                                count += int(maps[next_row][next_col])
                answer.append(count)
    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer