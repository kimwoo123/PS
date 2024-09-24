def solution(numbers, target):
    answer = 0
    l = len(numbers)
    stack = [(0, 0)]
    while stack:
        index, total = stack.pop()
        if index == l:
            if total == target:
                answer += 1
            continue
        stack.append((index + 1, total - numbers[index]))
        stack.append((index + 1, total + numbers[index]))
            
    return answer