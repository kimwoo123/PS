from heapq import heappush, heappop

def solution(operations):
    answer = [0, 0]
    min_queue = []
    max_queue = []
    count = dict()
    for operation in operations:
        command, number = operation.split()
        number = int(number)
        if command == "I":
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
            heappush(min_queue, number)
            heappush(max_queue, -1 * (number))
        else:
            if number == 1:
                while max_queue:
                    value = -1 * heappop(max_queue)
                    if count[value] != 0:
                        count[value] -= 1
                        break
            else:
                while min_queue:
                    value = heappop(min_queue)
                    if count[value] != 0:
                        count[value] -= 1
                        break
    while max_queue:
        value = -1 * heappop(max_queue)
        if count[value] != 0:
            answer[0] = value
            break
    
    while min_queue:
        value = heappop(min_queue)
        if count[value] != 0:
            answer[1] = value
            break
    
    return answer