def solution(n):
    answer = 0
    start, end = 1, 1
    total = 1
    while end <= n:
        if total >= n:
            if total == n:
                answer += 1
            total -= start
            start += 1
        elif total < n:
            end += 1
            total += end
    return answer