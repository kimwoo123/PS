import sys
input = sys.stdin.readline
from collections import deque

def main():
    N, K = map(int, input().split())

    cost_list = [1000000] * (K+1)
    if N > K:
        print(N - K)
        return
    cost_list[N] = 0

    queue = deque([(N, 0)])
    while queue:
        node, count = queue.popleft()
        for next_node, next_count in [(node+1, count+1), (node-1, count+1), (node*2, count)]:
            if 0 <= next_node < K+1 and cost_list[next_node] > next_count:
                cost_list[next_node] = next_count
                queue.append((next_node, next_count))
            elif next_node >= K+1:
                diff = next_count + (next_node - K)
                if cost_list[K] > diff:
                    cost_list[K] = diff

    print(cost_list[K])

if __name__ == "__main__":
    main()