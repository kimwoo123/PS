def solution(sequence, k):
    answer = [0, 1000000]
    start, end = 0, -1
    l = len(sequence)
    total = 0
    while start < l:
        if total == k:
            if end - start < answer[1] - answer[0]:
                answer[0], answer[1] = start, end
        if total < k:
            end += 1
            if end == l:
                break
            total += sequence[end]
        else:
            total -= sequence[start]
            start += 1

    return answer