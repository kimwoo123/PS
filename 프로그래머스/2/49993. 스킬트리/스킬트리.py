def solution(skill, skill_trees):
    answer = 0
    index_map = {s: i for i, s in enumerate(skill)}
    for skill_tree in skill_trees:
        flag = True
        visited = [0] * len(skill)
        for s in skill_tree:
            if s in index_map:
                index = index_map[s]
                if index != 0 and visited[index - 1] == 0:
                    flag = False
                    break
                visited[index] = 1
        if flag:
            answer += 1
            
    return answer