def solution(gems):
    answer = [0, 0]
    count_dict = {v: i for i, v in enumerate(set(gems))}
    l = len(gems)
    key_l = len(count_dict)
    
    start, end = 0, -1
    count_list = [0] * key_l
    while 0 in count_list:
        end += 1
        index = count_dict[gems[end]]
        count_list[index] += 1   
        
    before = start
    max_diff = 999999
    while end < l:
        if count_list[count_dict[gems[before]]] == 0:
            end += 1
            if end == l:
                break
            count_list[count_dict[gems[end]]] += 1
        else:
            diff = end - start
            if diff < max_diff:
                max_diff = diff
                answer[0], answer[1] = start+1, end+1
            count_list[count_dict[gems[start]]] -= 1
            before = start
            start += 1
        
    return answer