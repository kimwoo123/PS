import sys

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def solution():
    def start_index():
        flag = False
        result = set()
        for j in range(5, -1, -1):
            if board[11][j] != '.' and flag == False:
                flag = True
                result.add((11, j))
            else:
                 flag = False   
        return (result)

    def adj_more_four(row, col):
        color = board[row][col]
        count = 1
        history = {(row, col)}
        queue = {(row, col)}
        while (queue):
            next_p = set()
            for row, col in queue:
                for delta_row, delta_col in delta:
                    next_row = row + delta_row
                    next_col = col + delta_col
                    if 0 <= next_row < 12 and 0 <= next_col < 6:
                        if board[next_row][next_col] == color and (next_row, next_col) not in history:
                            next_p.add((next_row, next_col))
                            history.add((next_row, next_col))
                            count += 1
            queue = next_p
        if count >= 4:
            return history
        return set()

    def destroy_puyo(destroy_set):
        for row, col in destroy_set:
            board[row][col] = '.'
        for col in range(6):
            while (True):
                dot_index = 11
                block_index = 11
                for row in range(11, -1, -1):
                    if board[row][col] == '.':
                        dot_index = row
                        break
                for row in range(dot_index, -1, -1):
                    if board[row][col] != '.':
                        block_index = row
                        break
                if dot_index > block_index and board[dot_index][col] == '.' and board[block_index][col] != '.':
                    board[dot_index][col] = board[block_index][col]
                    board[block_index][col] = '.'
                else:
                    break   
            
    board = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
    count = 0
    while (True):
        queue = start_index()
        if not queue:
            print(count)
            break
        visited = [[0] * 6 for _ in range(12)]
        wait = set()
        while (queue):
            next_pos = set()
            for row, col in queue:
                for delta_row, delta_col in delta:
                    next_row = row + delta_row
                    next_col = col + delta_col
                    if 0 <= next_row < 12 and 0 <= next_col < 6:
                        if board[next_row][next_col] != '.' and visited[next_row][next_col] == 0:
                            visited[next_row][next_col] = 1
                            wait.update(adj_more_four(next_row, next_col))
                            next_pos.add((next_row, next_col))
            queue = next_pos
        if not wait:
            print(count)
            break
        destroy_puyo(wait)
        count += 1


if __name__ == "__main__":
    solution()