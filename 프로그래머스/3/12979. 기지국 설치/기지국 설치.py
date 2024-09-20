def solution(n, stations, w):
    answer = 0
    end = 0
    coverage = (w * 2) + 1
    for station in stations:
        s, e = station - w, station + w
        if end < s - 1:
            diff = s - end - 1
            answer += -(-diff // coverage)
        end = e
        
    if end < n:
        diff = n - end
        answer += -(-diff // coverage)
        
    return answer