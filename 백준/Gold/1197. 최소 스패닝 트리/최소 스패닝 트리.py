import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def get_ints():
    return map(int, input().split())

def find(a, parents):
    if parents[a] != a:
        parents[a] = find(parents[a], parents)
    return parents[a]

def union(a, b, parents):
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution():
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])

    parents = list(range(V+1))
    total = 0
    for a, b, c in edges:
        ap, bp = find(a, parents), find(b, parents)
        if ap != bp:
            union(ap, bp, parents)
            total += c

    print(total)

if __name__ == "__main__":
   solution()
