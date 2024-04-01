from sys import stdin
input = stdin.readline

def get_ints():
    return map(int, input().split())

def main():
    N, Q = get_ints()

    def make_time_format(string):
        return string[:4] + string[5:7] + string[8:10] + string[11:13] + string[14:16] + string[17:19]

    level_list = [[] for _ in range(7)]
    for _ in range(N):
        string, level = input().rstrip().split('#')
        level_list[int(level)].append(make_time_format(string))

    def bisect_left(level, time):
        target = level_list[level]
        start, end = 0, len(target)
        while start < end:
            mid = (start + end) // 2
            if target[mid] < time:
                start = mid + 1
            else:
                end = mid 
        return start

    def bisect_right(level, time):
        target = level_list[level]
        start, end = 0, len(target)
        while start < end:
            mid = (start + end) // 2
            if target[mid] > time:
                end = mid
            else:
                start = mid + 1
        return start

    for _ in range(Q):
        start, end, level = input().rstrip().split('#')
        start = make_time_format(start)
        end = make_time_format(end)
        level = int(level)
        result = 0
        for l in range(level, 7):
            s = bisect_left(l, start)
            e = bisect_right(l, end)
            result += (e - s)
        print(result)

if __name__ == "__main__":
    main()