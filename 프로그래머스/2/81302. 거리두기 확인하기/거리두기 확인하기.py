def manhatan_distance(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2)


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(place, visited, start_row, start_col):
    visited[start_row][start_col] = 1
    stack = [(start_row, start_col)]
    while stack:
        row, col = stack.pop()
        for delta_row, delta_col in delta:
            next_row = row + delta_row
            next_col = col + delta_col
            if 0 <= next_row < 5 and 0 <= next_col < 5:
                if manhatan_distance(start_row, start_col, next_row, next_col) > 2:
                    continue
                if visited[next_row][next_col] == 0:
                    if place[next_row][next_col] == "P":
                        return False
                    if place[next_row][next_col] == "O":
                        visited[next_row][next_col] = 1
                        stack.append((next_row, next_col))
    return True

def check_distance(place):
    visited = [[0] * 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if place[row][col] == "P":
                ret = dfs(place, visited, row, col)
                if ret == False:
                    return 0
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(check_distance(place))
        
    return answer