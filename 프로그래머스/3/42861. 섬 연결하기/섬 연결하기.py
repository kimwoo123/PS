def find(a, parents):
    while a != parents[a]:
        a, parents[a] = parents[a], parents[parents[a]]
    return a

def union(a, b, parents):
    a = find(a, parents)
    b = find(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, costs):
    answer = 0
    parents = list(range(n + 1))
    costs.sort(key=lambda x:x[2])
    for a, b, cost in costs:
        if find(a, parents) != find(b, parents):
            answer += cost
            union(a, b, parents)

    return answer