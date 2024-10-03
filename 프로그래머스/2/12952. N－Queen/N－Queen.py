delta = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def is_edible(board, row, col, n):
    for i in range(row):
        if board[row] == board[i] or abs(row-i) == abs(board[row] - board[i]):
            return False
    
    return True

answer = 0
def backtrack(board, n, index, visited):
    if index == n:
        global answer
        answer += 1
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            board.append(i)
            if is_edible(board, index, i, n):
                backtrack(board, n, index + 1, visited)
            board.pop()
            visited[i] = 0

def solution(n):
    board = []
    visited = [0] * n
    backtrack(board, n, 0, visited)
    
    return answer