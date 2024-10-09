def get_permutations(numbers, visited, index, l, ret):
    if index == 0:
        yield int(ret)
    for i in range(l):
        if visited[i] == 0:
            visited[i] = 1
            yield from get_permutations(numbers, visited, index - 1, l, ret + numbers[i])
            visited[i] = 0
    
def solution(numbers):
    l = len(numbers)
    ll = 10 ** l
    
    erasto = [1] * ll
    erasto[0], erasto[1] = 0, 0
    end = int(ll ** 0.5) + 1
    for i in range(2, end):
        if erasto[i] == 0:
            continue
        for j in range(i * 2, ll, i):
            erasto[j] = 0
            
    answer = set()
    visited = [0] * l
    for i in range(1, l+1):
        for perm in get_permutations(numbers, visited, i, l, ''):
            if erasto[perm] and perm not in answer:
                answer.add(perm)
            
    return len(answer)