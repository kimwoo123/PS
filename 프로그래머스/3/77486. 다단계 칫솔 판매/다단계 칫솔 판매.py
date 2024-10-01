def solution(enroll, referral, seller, amount):
    l = len(enroll)
    answer = [0] * l
    refer_from = {k: v for k, v in zip(enroll, referral)}
    index_from = {k: i for i, k in enumerate(enroll)}
    
    for s,a in zip(seller, amount):
        benefit = a * 100
        node = s
        while node != '-' and benefit:
            index = index_from[node] 
            answer[index] += benefit - (benefit // 10)
            benefit //= 10
            node = refer_from[node]
    
    return answer