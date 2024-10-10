def solution(number, k):
    answer = 0
    l = len(number)
    stack = []
    for n in number:
        while stack and stack[-1] < n and k:
            del stack[-1]
            k -= 1
        stack.append(n)
    
    for i in range(k):
        stack.pop()
        
    return ''.join(stack)