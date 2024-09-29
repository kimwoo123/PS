def solution(phone_book):
    
    number_set = set(phone_book)
    for number in phone_book:
        prefix = ""
        for n in number:
            prefix += n
            if prefix in number_set and prefix != number:
                return False
    
    return True