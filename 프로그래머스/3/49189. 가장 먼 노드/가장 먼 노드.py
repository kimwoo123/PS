def solution(n, edge):
    answer = 0
    adj_list = [[] for _ in range(n+1)]
    for a, b in edge:
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    
    visited = [0] * (n+1)
    visited[1] = 1
    queue = [(1, 0)]
    max_count = 0
    while queue:
        node, count = queue.pop(0)
        if count > max_count:
            max_count = count
            answer = 1
        elif count == max_count:
            answer += 1
        for next_node in adj_list[node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                queue.append((next_node, count + 1))
            
        
    return answer