from heapq import heappush, heappop

def solution(jobs):
    time = 0
    index = 0
    l = len(jobs)
    heap = []
    current = 0
    jobs.sort()
    while index < l or heap:
        while index < l and jobs[index][0] <= current:
            s, e = jobs[index]
            heappush(heap, (e, s))
            index += 1
            
        if heap:
            e, s = heappop(heap)
            time += current - s + e
            current += e
        else:
            current = jobs[index][0]
            
    return time // l