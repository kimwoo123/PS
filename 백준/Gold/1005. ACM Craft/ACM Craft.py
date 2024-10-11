import sys
input = sys.stdin.readline

def get_ints():
    return map(int, input().split())

def solution():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        time_list = tuple(map(int, input().split()))

        graph = [[] for _ in range(N+1)]
        indegree = [[0, 0] for _ in range(N+1)]
        for _ in range(K):
            a, b = map(int, input().split())
            graph[a].append(b)
            indegree[b][0] += 1

        dest = int(input())
        queue = [(i, 0) for i in range(1, N+1) if indegree[i][0] == 0]
        while queue:
            node, count = queue.pop(0)
            count += time_list[node - 1]
            if node == dest:
                print(count)
                break
            for next_node in graph[node]:
                if indegree[next_node][1] < count:
                    indegree[next_node][1] = count
                indegree[next_node][0] -= 1
                if indegree[next_node][0] == 0:
                    queue.append((next_node, indegree[next_node][1]))

if __name__ == "__main__":
   solution()
