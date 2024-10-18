import sys
input = sys.stdin.readline

def main():
    N, M, X = map(int, input().split())

    go_graph = [[] for _ in range(N+1)]
    back_graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, cost = map(int, input().split())
        go_graph[start].append((end, cost))
        back_graph[end].append((start, cost))

    dist_list = [100001] * (N+1)
    dist_list[X] = 0
    queue = [(X, 0)]
    while queue:
        node, total = queue.pop(0)
        for next_node, cost in go_graph[node]:
            if dist_list[next_node] > total + cost:
                dist_list[next_node] = total + cost
                queue.append((next_node, total + cost))


    dist_list2 = [100001] * (N+1)
    dist_list2[X] = 0
    queue = [(X, 0)]
    while queue:
        node, total = queue.pop(0)
        for next_node, cost in back_graph[node]:
            if dist_list2[next_node] > total + cost:
                dist_list2[next_node] = total + cost
                queue.append((next_node, total + cost))

    print(max(map(sum, zip(dist_list[1:], dist_list2[1:]))))

if __name__ == "__main__":
    main()