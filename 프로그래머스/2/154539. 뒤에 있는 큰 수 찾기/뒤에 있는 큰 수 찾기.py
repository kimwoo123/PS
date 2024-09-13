def solution(numbers):
    l = len(numbers)
    answer = [-1] * l
    stack = []
    for i in range(l):
        while stack and stack[-1][0] < numbers[i]:
            _, index = stack.pop()
            answer[index] = numbers[i]
        stack.append((numbers[i], i))
        
    return answer