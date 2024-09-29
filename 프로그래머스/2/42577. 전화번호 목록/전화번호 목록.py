def strcmp(s1, s2):
    l = min(len(s1), len(s2))
    for i in range(l):
        if s1[i] != s2[i]:
            return False
    return True

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if strcmp(phone_book[i], phone_book[i+1]):
            return False
    
    return True