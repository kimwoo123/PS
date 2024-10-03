def solution(s):
    t = tuple(map(int, s.split()))
    answer = str(min(t)) + ' ' + str(max(t))
    return answer