def solution(elements):
    answer = 0
    l = len(elements)
    circle = elements * 2
    cumulative = [0] * (l * 2)
    cumulative[0] = elements[0]
    for i in range(1, l * 2):
        cumulative[i] = cumulative[i-1] + circle[i]
        
    visit = set()
    for length in range(1, l + 1):
        for i in range(l):
            s = cumulative[i + length] - cumulative[i]
            visit.add(s)
    
    return len(visit)