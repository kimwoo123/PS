from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(((p, i) for i, p in enumerate(priorities)))
    while True:
        max_value = max(queue, key=lambda x:x[0])[0]
        while queue[0][0] != max_value:
            queue.rotate(-1)
        answer += 1
        index = queue.popleft()
        if index[1] == location:
            return answer