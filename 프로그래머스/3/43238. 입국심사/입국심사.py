def solution(n, times):
    answer = 0
    max_time = max(times) * n
    start, end = 0, max_time
    while start + 1 != end:
        mid = (start + end) // 2
        s = sum(mid // time for time in times)
        if s >= n:
            end = mid
        else:
            start = mid
        
    return end