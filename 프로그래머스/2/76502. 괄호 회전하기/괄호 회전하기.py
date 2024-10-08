def solution(s):
    answer = 0
    open_ = ('(', '{', '[')
    close_ = (')', '}', ']')
    map_ = {
        '(': ')',
        '{': '}',
        '[': ']',
    } 
    stack = []
    for i in range(len(s)):
        n = list(s[i:] + s[:i])
        while n:
            if n[-1] in open_ and stack and stack[-1] == map_[n[-1]]:
                del stack[-1], n[-1]
            else:
                stack.append(n.pop())
        if not stack:
            answer += 1
        stack.clear()
    return answer