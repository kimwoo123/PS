import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    queue = [i for i in range(1, N+1) if indegree[i] == 0]
    answer = []
    while queue:
        node = queue.pop(0)
        answer.append(node)
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    print(*answer)



if __name__ == "__main__":
   solution()
