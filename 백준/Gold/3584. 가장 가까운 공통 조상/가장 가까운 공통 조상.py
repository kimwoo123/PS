from sys import stdin, setrecursionlimit
input = stdin.readline

def get_ints():
    return map(int, input().split())

def main():
    setrecursionlimit(1000000)
    T = int(input())
    for _ in range(T):
        N = int(input())
        parents = list(range(N+1))
        depths = [0] * (N+1)
        visited = [0] * (N+1)
        adj_list = [[] for _ in range(N+1)]
        root = [0] * (N)
        for _ in range(N-1):
            a, b = get_ints()
            adj_list[a].append(b)
            root[b-1] = 1

        query = tuple(get_ints())
        def dfs(node, depth):
            visited[node] = 1
            depths[node] = depth
            for next_node in adj_list[node]:
                if visited[next_node] == 0:
                    parents[next_node] = node
                    dfs(next_node, depth + 1)

        dfs(root.index(0) + 1, 1)

        def lca(a, b):
            while depths[a] != depths[b]:
                if depths[a] < depths[b]:
                    b = parents[b]
                else:
                    a = parents[a]

            while a != b:
                a = parents[a]
                b = parents[b]
            
            return a
        print(lca(query[0], query[1]))

if __name__ == "__main__":
    main()