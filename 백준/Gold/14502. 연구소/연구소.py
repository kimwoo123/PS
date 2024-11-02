from collections import deque

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

virus_list = []
safe_area = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
           virus_list.append([i, j])
        elif matrix[i][j] == 0:
            safe_area += 1
result = 0


def create_wall(wall_counts):
    if wall_counts == 3:
        temp_matrix = [row[:] for row in matrix]
        count_virus(temp_matrix)
    else:
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    create_wall(wall_counts + 1)
                    matrix[i][j] = 0


def count_virus(temp_matrix):
    stack = deque([row[:] for row in virus_list])

    while stack:
        row, col = stack.popleft()
        for delta_row, delta_col in delta:
            next_row = row + delta_row
            next_col = col + delta_col
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M:
                continue
            if temp_matrix[next_row][next_col] == 0:
                temp_matrix[next_row][next_col] = 2
                stack.append([next_row, next_col])

    count = 0
    for i in range(N):
        count += temp_matrix[i].count(0)

    global result
    result = max(result, count)

create_wall(0)
print(result)