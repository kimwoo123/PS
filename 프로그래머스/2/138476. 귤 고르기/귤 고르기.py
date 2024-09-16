def solution(k, tangerine):
    answer = 0
    count = dict()
    
    for t in tangerine:
        if t in count:
            count[t] += 1
        else:
            count[t] = 1
    
    for v in sorted(count.values(), reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            break
    
    return answer