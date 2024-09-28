def solution(prices):
    answer = list(range(len(prices)-1, -1, -1))
    stack = []
    for i, p in enumerate(prices):
        while stack and stack[-1][1] > p:
            index, _ = stack.pop()
            answer[index] = i - index
        stack.append((i, p))
        
    return answer