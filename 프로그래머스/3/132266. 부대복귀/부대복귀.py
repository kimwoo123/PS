def solution(n, roads, sources, destination):
    dist_list = [-1 for _ in range(n+1)]
    adj_list = [[] for _ in range(n+1)]
    for a, b in roads:
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    queue = [(destination, 0)]
    while queue:
        node, count = queue.pop(0)
        dist_list[node] = count
        for next_node in adj_list[node]:
            if dist_list[next_node] == -1:
                dist_list[next_node] = count + 1
                queue.append((next_node, count + 1))
    
    return tuple(dist_list[s] for s in sources)