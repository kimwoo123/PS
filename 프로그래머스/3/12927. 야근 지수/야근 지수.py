from heapq import heappush, heappop, heapify

def solution(n, works):
    answer = 0
    works = list(map(lambda x: -x, works))
    heapify(works)
    for _ in range(n):
        value = heappop(works)
        if value == 0:
            heappush(works, 0)
            break
        heappush(works, value + 1)
    answer = sum(map(lambda x: x ** 2, works))
    return answer