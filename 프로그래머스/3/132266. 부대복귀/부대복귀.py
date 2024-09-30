def solution(n, roads, sources, destination):
    dist_list = [500000 for _ in range(n+1)]
    adj_list = [[] for _ in range(n+1)]
    for a, b in roads:
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    visited = [0] * (n+1)
    queue = [(destination, 0)]
    while queue:
        node, count = queue.pop(0)
        if dist_list[node] > count:
            dist_list[node] = count
        for next_node in adj_list[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append((next_node, count + 1))
    
    answer = []
    for s in sources:
        if dist_list[s] == 500000:
            answer.append(-1)
        else:
            answer.append(dist_list[s])
            
    return answer