from math import floor

def make_set(s):
    ret = dict()
    s = s.lower()
    for i in range(len(s) - 1):
        temp = s[i:i+2]
        if temp.isalpha():
            if temp in ret:
                ret[temp] += 1
            else:
                ret[temp] = 1
    return ret
        

def solution(str1, str2):
    answer = 0
    s1, s2 = make_set(str1), make_set(str2)
    k1, k2 = set(s1.keys()), set(s2.keys())
    
    a = 0
    for e in k1 & k2:
        a += min(s1.get(e, 0), s2.get(e, 0))
    
    b = 0
    for e in k1 | k2:
        b += max(s1.get(e, 0), s2.get(e, 0))
            
    if a == b:
        answer = 1
    else:
        answer = a / b
    return floor(answer * 65536)