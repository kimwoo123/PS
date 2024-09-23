def solution(dirs):
    answer = 0
    delta_map = {
        "U": (-1, 0),
        "L": (0, -1),
        "R": (0, 1),
        "D": (1, 0),
    }
    visited = set()
    row, col = 0, 0
    for dir_ in dirs:
        delta_row, delta_col = delta_map[dir_]
        next_row = row + delta_row
        next_col = col + delta_col
        if -5 <= next_row <= 5 and -5 <= next_col <= 5:
            node = tuple(sorted([(row, col), (next_row, next_col)]))
            if node not in visited:
                visited.add(node)
                answer += 1
            row, col = next_row, next_col
            
    return answer