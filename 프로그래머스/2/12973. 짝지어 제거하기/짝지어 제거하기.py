def solution(s):
    s = list(s)
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            del stack[-1]
        else:
            stack.append(c)
    if len(stack):
        return 0
    return 1