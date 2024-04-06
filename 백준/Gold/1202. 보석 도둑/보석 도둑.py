from sys import stdin
input = stdin.readline


def get_ints():
    return map(int, input().split())

def get_int():
    return int(input())

from heapq import heapify, heappop, heappush

def main():
    N, K = get_ints()
    jewel_list = sorted([tuple(get_ints()) for _ in range(N)], reverse=True)
    bag_list = sorted([get_int() for _ in range(K)])

    max_heap = []
    result = 0
    for bag in bag_list:
        while jewel_list and jewel_list[-1][0] <= bag:
            heappush(max_heap, -jewel_list.pop()[1])
        if max_heap:
            result += -heappop(max_heap)

    print(result)

if __name__ == "__main__":
    main()