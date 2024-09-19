def solution(n, wires):
    answer = 9999
    adj_list = [[] for _ in range(n + 1)]
    for a, b in wires:
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    def bfs(start_node, visited, no_a, no_b):
        queue = [start_node]
        visited[start_node] = 1
        count = 1
        while queue:
            node = queue.pop(0)
            for next_node in adj_list[node]:
                if node == no_a and next_node == no_b:
                    continue
                if node == no_b and next_node == no_b:
                    continue
                if visited[next_node] == 0:
                    count += 1
                    visited[next_node] = 1
                    queue.append(next_node)
        return count
        
        
    for no_a, no_b in wires:
        visited = [0] * (n + 1)
        a_count = bfs(no_a, visited, no_a, no_b)
        b_count = bfs(no_b, visited, no_a, no_b)
        if a_count + b_count == n:
            diff = abs(a_count - b_count)
            if diff < answer:
                answer = diff
        
    return answer