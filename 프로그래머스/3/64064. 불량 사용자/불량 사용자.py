def strcmp(s1, s2):
    l = len(s1)
    if l != len(s2):
        return False
    for i in range(l):
        if s2[i] != '*' and (s1[i] != s2[i]):
            return False
    return True

def solution(user_id, banned_id):
    count = 0
    l = len(user_id)
    visited = [0] * l
    visit_set = set()
    ban_l = len(banned_id)
    def dfs(index, ban_list):
        if index == ban_l:
            temp = tuple(sorted(ban_list))

            if temp not in visit_set:
                visit_set.add(temp)
                nonlocal count
                count += 1
            return
        for i in range(l):
            if visited[i] == 0 and (strcmp(user_id[i], banned_id[index])):
                visited[i] = 1
                ban_list.append(i)
                dfs(index + 1, ban_list)
                ban_list.pop()
                visited[i] = 0
    dfs(0, [])
        
    return count