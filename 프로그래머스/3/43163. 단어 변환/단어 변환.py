def diff_one_char(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    if count == 1:
        return True
    return False
    

def solution(begin, target, words):
    answer = 99999
    l = len(words)
    visited = [0] * l
    
    def dfs(current, count):
        if current == target:
            nonlocal answer
            if answer > count:
                answer = count
            return
        for i in range(l):
            if diff_one_char(current, words[i]) and visited[i] == 0:
                visited[i] = 1
                dfs(words[i], count + 1)
                visited[i] = 0
    
    dfs(begin, 0)
    if answer == 99999:
        return 0
    return answer