def compare(info, l_info):
    total = [0, 0]
    score = 10
    for a, l in zip(info, l_info):
        if a > l:
            total[0] += score
        elif a < l:
            total[1] += score
        score -= 1
    return total[1] - total[0]
    
def solution(n, info):
    answer = []
    
    max_value = 0
    def DFS(arrows, index, l_info):
        if index == -1:
            ret = compare(info, l_info)
            nonlocal max_value
            if ret > 0 and ret > max_value:
                nonlocal answer
                max_value = ret
                answer = l_info[:]
                answer[-1] = arrows
            return
        need_arrow = info[index] + 1
        if arrows >= need_arrow:
            l_info[index] = need_arrow
            DFS(arrows - need_arrow, index - 1, l_info)
            l_info[index] = 0
        DFS(arrows, index - 1, l_info)
    
    DFS(sum(info), 10, [0] * 11)
    if max_value == 0:
        return [-1]
    return answer