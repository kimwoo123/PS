def get_combos(rel_list, index, count, ret):
    if count == 0:
        yield ret
    for i in range(index, len(rel_list)):
        ret.append(rel_list[i])
        yield from get_combos(rel_list, i+1, count-1, ret)
        ret.pop()

def solution(relation):
    answer = 0
    l = len(relation[0])
    zip_rel = list(zip(*relation))
    r = list(range(l))
    visited = []
    
    for i in range(1, l):
        for combo in get_combos(r, 0, i, []):
            table = (zip_rel[row] for row in combo)
            t_lst = list(zip(*table))
            t_set = set(t_lst)
            if len(t_lst) == len(t_set):
                key = set(combo)
                for v in visited:
                    if v.issubset(key):
                        break
                else:
                    visited.append(key)
                    answer += 1
    if answer == 0:
        return 1
    
    return answer