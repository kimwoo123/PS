
def find_start(row_len, col_len, maps):
    for i in range(row_len):
        for j in range(col_len):
            if maps[i][j] == "S":
                return (i, j)
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]            
def find_lever(row_len, col_len, start, maps, dest):
    visited = [[0] * col_len for _ in range(row_len)]
    visited[start[0]][start[1]] = 1
    queue = [start + (0,)]
    while queue:
        row, col, count = queue.pop(0)
        if maps[row][col] == dest:
            if dest == "L":
                temp = find_lever(row_len, col_len, (row, col), maps, "E")
                if temp != -1:
                    return count + temp
                return -1
            else:
                return count
        for delta_row, delta_col in delta:
            next_row = row + delta_row
            next_col = col + delta_col
            if 0 <= next_row < row_len and 0 <= next_col < col_len:
                if visited[next_row][next_col] == 0 and maps[next_row][next_col] != "X":
                    visited[next_row][next_col] = 1
                    queue.append((next_row, next_col, count + 1))
    return -1
            
def solution(maps):
    answer = -1
    row_len = len(maps)
    col_len = len(maps[0])
    
    start = find_start(row_len, col_len, maps)
    answer = find_lever(row_len, col_len, start, maps, "L")
    return answer