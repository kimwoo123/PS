def strcmp(s1, s2):
    l = min(len(s1), len(s2))
    for i in range(l):
        if s1[i] != s2[i]:
            return False
    return True

def solution(phone_book):
    phone_book.sort()
    index1, index2 = 0, 0
    l = len(phone_book)
    for i in range(l - 1):
        if strcmp(phone_book[i], phone_book[i+1]):
            return False
    
    return True