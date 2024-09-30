def solution(s):
    l = len(s)
    for j in range(l, 0, -1):
        for i in range(l - j + 1):
            temp = s[i:i+j]
            if temp == temp[::-1]:
                return j