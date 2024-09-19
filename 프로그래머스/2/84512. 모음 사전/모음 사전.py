def solution(word):
    answer = 0
    moum = ('A', 'E', 'I', 'O', 'U')
    g_count = 0
    def dfs(current, index, count):
        nonlocal g_count
        if current == word:
            nonlocal answer
            answer = g_count
            return
        if index == 5:
            return
        for c in moum:
            g_count += 1
            dfs(current + c, index + 1, count + 1)
    
    dfs('', 0, 0,)
    
    return answer