def solution(numbers):
    l = len(numbers)
    answer = [-1] * l
    stack = []
    for i in range(l):
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()
            answer[index] = numbers[i]
        stack.append(i)
        
    return answer