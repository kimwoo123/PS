def is_block(row, col, board):
    c = board[row][col]
    for i in range(row, row+2):
        for j in range(col, col+2):
            if board[i][j] != c:
                return False
    return True

def destroy_block(pending, board):
    count = 0
    for row, col in pending:
        for i in range(row, row + 2):
            for j in range(col, col + 2):
                if board[i][j] != None:
                    count += 1
                board[i][j] = None
    return count
    
def find_block(m, n, pending, board):
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] and is_block(i, j, board):
                pending.append((i, j))
    
def falling_block(m, n, board):
    for i in range(n-1, -1, -1):
        block_list = []
        for j in range(m-1, -1, -1):
            if board[j][i] != None:
                block_list.append(board[j][i])
        index = 0
        for j in range(m-1, -1, -1):
            if index < len(block_list):
                board[j][i] = block_list[index]
                index += 1
            else:
                board[j][i] = None
        
    
def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    
    while True:
        pending = []
        find_block(m, n, pending, board)
        answer += destroy_block(pending, board)
        falling_block(m, n, board)
        if pending == []:
            break
    
    
    return answer