from collections import deque

def solution(s):
    answer = 0
    d = deque(s)
    open_ = ('(', '{', '[')
    close_ = (')', '}', ']')
    map_ = {
        '(': ')',
        '{': '}',
        '[': ']',
    } 
    stack = []
    for _ in s:
        d.rotate()
        n = d.copy()
        while n:
            if n[-1] in open_ and stack and stack[-1] == map_[n[-1]]:
                del stack[-1], n[-1]
            else:
                stack.append(n.pop())
        if not stack:
            answer += 1
        stack.clear()
    return answer