from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    l = len (scoville)
    heapify(scoville)
    while K > scoville[0]:
        if l == 1:
            return -1
        a, b = heappop(scoville), heappop(scoville)
        heappush(scoville, a + (b * 2))
        answer += 1
        l -= 1

    
    return answer