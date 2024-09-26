def solution(citations):
    citations.sort(reverse=True)
    if citations[0] == 0:
        return 0
    l = len(citations)
    for i in range(l - 1):
        if citations[i] >= i + 1 >= citations[i+1]:
            return i + 1
    return l