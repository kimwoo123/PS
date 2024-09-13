from collections import deque

def solution(x, y, n):
    answer = 9999
    visited = set()
    queue = deque([(x, 0)])
    while queue:
        value, count = queue.popleft()
        if value == y:
            if answer > count:
                answer = count
            continue
        if value > y or value in visited:
            continue
        visited.add(value)
        queue.append((value * 3, count + 1))
        queue.append((value * 2, count + 1))
        queue.append((value + n, count + 1))
    
    if answer == 9999:
        return -1
    return answer