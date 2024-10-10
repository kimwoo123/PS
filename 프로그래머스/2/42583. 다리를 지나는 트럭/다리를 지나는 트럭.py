from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([(truck_weights[0], bridge_length)])
    current = truck_weights[0]
    for w in truck_weights[1:]:
        answer += 1
        if queue and current + w > weight:
            while queue and current + w > weight:
                w_, time = queue.popleft()
                answer = max(time, answer)
                current -= w_
            queue.append((w, answer + bridge_length))
            current += w
        else:
            current += w            
            queue.append((w, answer + bridge_length))
    
        # print(queue, answer)
    if queue:
        return queue[-1][1] + 1
    return answer