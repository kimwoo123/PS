from collections import Counter

def solution(topping):
    answer = 0
    count = Counter(topping)
    elder_set = set()
    elder_count = 0
    older_count = len(count)
    for i in range(len(topping) - 1, -1, -1):
        key = topping[i]
        count[key] -= 1
        if key not in elder_set:
            elder_set.add(key)
            elder_count += 1
        if count[key] == 0:
            older_count -= 1
            
        if elder_count == older_count:
            answer += 1
        if elder_count > older_count:
            break
            
    return answer