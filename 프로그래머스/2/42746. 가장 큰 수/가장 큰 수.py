from functools import cmp_to_key

def cmp(s1, s2):
    temp1 = int(s1 + s2)
    temp2 = int(s2 + s1)
    return temp1 - temp2        

def solution(numbers):
    return str(int(''.join(sorted(map(str, numbers), key=cmp_to_key(cmp), reverse=True))))
    