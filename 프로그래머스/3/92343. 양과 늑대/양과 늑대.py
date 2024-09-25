def solution(info, edges):
    answer = 0
    l = len(info)
    adj_list = [[] for _ in range(l)]
    for a, b in edges:
        adj_list[a].append(b)
        
    def dfs(current, nodes, score, sheep):
        if score <= 0:
            return
        nonlocal answer
        if sheep > answer:
            answer = sheep
        for i in range(len(nodes)):
            next_nodes = nodes[:]
            next_node = next_nodes.pop(i)
            next_nodes.extend(adj_list[next_node])
            if info[next_node] == 0:
                dfs(next_node, next_nodes, score + 1, sheep + 1)
            else:
                dfs(next_node, next_nodes, score - 1, sheep)

    dfs(0, adj_list[0], 1, 1)
    
    return answer