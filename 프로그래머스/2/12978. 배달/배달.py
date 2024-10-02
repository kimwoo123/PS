def solution(N, road, K):
    answer = 0
    
    adj_list =[[] for _ in range(N+1)]
    for a, b, c in road:
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))

    queue = [(1, 0)]
    dist_list = [9999999] * (N + 1)
    dist_list[1] = 0
    while queue:
        node, count = queue.pop(0)
        for next_node, add_count in adj_list[node]:
            total = count + add_count
            if dist_list[next_node] > total:
                dist_list[next_node] = total
                queue.append((next_node, total))

    for i in range(1, N + 1):
        if dist_list[i] <= K:
            answer += 1
    return answer