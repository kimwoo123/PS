def solution(targets):
    answer = 0
    targets.sort()
    before = [500000, 500000]
    for s, e in targets:
        if s >= before[0] and s < before[1]:
            before[0] = s
            if before[1] > e:
                before[1] = e
        else:
            before[0], before[1] = s, e
            answer += 1
        
    return answer