from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    heap = []
    index = 0
    l = len(enemy)
    while True:
        if n >= enemy[index]:
            n -= enemy[index]
            heappush(heap, -enemy[index])
            answer += 1
            index += 1
            if index == l:
                break
        else:
            if k:
                k -= 1
                heappush(heap, -enemy[index])
                n -= enemy[index]
                value = -1 * heappop(heap)
                n += value
                answer += 1
                index += 1
                if index == l:
                    break
            else:
                break
                
    return answer