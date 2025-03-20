def calculate(diffs, times, level, n, limit):
    total = 0
    before = 0
    for i in range(n):
        diff, time = diffs[i], times[i]
        if diff <= level:
            total += time
        else:
            total += (diff - level) * (time + before) + time
    
        before = time
        if total > limit:
            return False
        
    return True
        

def solution(diffs, times, limit):
    answer = 300_000
    n = len(diffs)
    
    left = 0
    right = 300_000
    while left < right - 1:
        mid = (left + right) // 2
        if calculate(diffs, times, mid, n, limit):
            answer = mid
            right = mid
        else:
            left = mid
    
    return answer