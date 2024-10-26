import sys

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    parent, child = map(int, sys.stdin.readline().split())
    tree[parent].append(child)
    tree[child].append(parent)

parents = [[] for _ in range(N + 1)]

def DFS(root, tree, parents):
    stack = [root]
    while stack:
        node = stack.pop()
        for i in tree[node]:
            parents[i].append(node)
            stack.append(i)
            tree[i].remove(node)

DFS(1, tree, parents)

for i in range(2, N + 1):
    print(parents[i][0])