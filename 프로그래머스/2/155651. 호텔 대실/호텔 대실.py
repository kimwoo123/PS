from heapq import heappush, heappop

def str_to_time(s):
    hh, mm = s.split(':')
    return int(hh) * 60 + int(mm)

def solution(book_time):
    answer = 0
    book_time.sort()
    heap = []
    count = 0
    for start, end in book_time:
        start, end = str_to_time(start), str_to_time(end)
        while heap and heap[0] + 10 <= start:
            heappop(heap)
            count -= 1
        heappush(heap, end)
        count += 1
        if count > answer:
            answer = count
    return answer