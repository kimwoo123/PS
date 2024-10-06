def check(want_dict):
    for k, v in want_dict.items():
        if v > 0:
            return False
    return True

def solution(want, number, discount):    
    want_dict = dict(zip(want, number))
    for i in range(10):
        key = discount[i]
        if key in want_dict:
            want_dict[key] -= 1

    answer = 0
    if check(want_dict):
        answer += 1
            
    for i in range(len(discount) - 10):
        key = discount[i]
        if key in want_dict:
            want_dict[key] += 1
            
        next_key = discount[i+10]
        if next_key in want_dict:
            want_dict[next_key] -= 1

        if check(want_dict):
            answer += 1
        
    return answer