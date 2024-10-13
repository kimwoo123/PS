def count_one(s):
    count = 0
    for c in s:
        if c == '1':
            count += 1
            
    return count

def solution(n):
    count = count_one(str("{0:b}".format(n)))
    while n:
        n += 1
        temp = str("{0:b}".format(n))
        if count == count_one(temp):
            return n
