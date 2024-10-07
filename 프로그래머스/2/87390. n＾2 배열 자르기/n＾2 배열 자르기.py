def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        temp = max(i // n, i % n) + 1
        answer.append(temp)
    return answer