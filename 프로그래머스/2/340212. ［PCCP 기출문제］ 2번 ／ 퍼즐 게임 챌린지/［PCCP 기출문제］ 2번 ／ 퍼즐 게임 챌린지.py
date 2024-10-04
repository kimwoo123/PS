def solve_puzzle(level, diffs, times, limit):
    total = 0
    before = 0
    for diff, time_cur in zip(diffs, times):
        if diff <= level:
            total += time_cur
        else:
            c = diff - level 
            total += (time_cur + before) * c + time_cur
        if total > limit:
            return -1
        before = time_cur
    return 1

def solution(diffs, times, limit):
    start, end = 0, max(diffs)
    while start + 1 != end:
        mid = (start + end) // 2
        level = solve_puzzle(mid, diffs, times, limit)
        if level > 0:
            end = mid
        else:
            start = mid
    return end