def traverse(node, graph, cards, group):
    count = 0
    while graph[node] == 0:
        count += 1
        graph[node] = group
        node = cards[node - 1]
    return count
        
def solution(cards):
    answer = []
    
    graph = [0] * (len(cards) + 1)
    group = 1
    for c in cards:
        if graph[c] == 0:
            count = traverse(c, graph, cards, group)
            answer.append(count)
            group += 1
        
    answer.sort(reverse=True)
    if len(answer) < 2:
        return 0
    return answer[0] * answer[1]