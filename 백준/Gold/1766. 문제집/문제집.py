from sys import stdin
input = stdin.readline

def get_ints():
    return map(int, input().split())

from heapq import heappush, heappop

def main():
    N, M = get_ints()
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = get_ints()
        indegree[b] += 1
        graph[a].append(b)

    heap = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            heappush(heap, i)
            
    result = []
    while heap:
        node = heappop(heap)
        result.append(node)
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                heappush(heap, next_node)

    print(*result) 

if __name__ == "__main__":
    main()