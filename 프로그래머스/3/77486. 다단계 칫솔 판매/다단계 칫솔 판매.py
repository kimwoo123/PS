def solution(enroll, referral, seller, amount):
    refer_from = {k: v for k, v in zip(enroll, referral)}
    answer = {k: 0 for k in enroll}
    
    for s,a in zip(seller, amount):
        benefit = a * 100
        node = s
        while node != '-' and benefit:
            answer[node] += benefit - (benefit // 10)
            benefit //= 10
            node = refer_from[node]
    
    return list(answer.values())