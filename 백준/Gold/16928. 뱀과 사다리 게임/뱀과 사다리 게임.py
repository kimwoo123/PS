from collections import deque
import sys

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        point = queue.popleft()
        for i in range(1, 7):
            next_point = point + i
            if next_point > 100:
                continue
            if next_point in ladder_snake.keys():
                next_point = ladder_snake[next_point]
            if not visited[next_point]:
                queue.append(next_point)
                visited[next_point] = True
                check_board[next_point] = check_board[point] + 1




N, M = map(int, input().split())
ladder_snake = dict()

for _ in range(N):
    start, end = map(int, input().split())
    ladder_snake[start] = end

for _ in range(M):
    start, end = map(int, input().split())
    ladder_snake[start] = end


visited = [False] * 101
check_board = [0] * 101
bfs()
print(check_board[100])