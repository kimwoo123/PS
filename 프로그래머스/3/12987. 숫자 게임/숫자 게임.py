from heapq import heappush, heappop

def solution(A, B):
    answer = 0
    a_heap = []
    b_heap = []
    for i in range(len(A)):
        heappush(a_heap, -A[i])
        heappush(b_heap, -B[i])
    
    while a_heap and b_heap:
        if a_heap[0] > b_heap[0]:
            heappop(a_heap)
            heappop(b_heap)
            answer += 1
        else:
            heappop(a_heap)
    
    return answer