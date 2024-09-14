def solution(storey):
    answer = 0
    number = storey
    while number:
        remain = number % 10 
        number //= 10
        if remain > 5 or (remain == 5 and number % 10 >= 5):
            number += 1
            answer += (10 - remain)
        else:
            answer += remain
    return answer