def solution(users, emoticons):
    answer = [0, 0]
    
    l = len(emoticons)
    def backtrack(index, l, percent_list):
        if index == l:
            calcul(percent_list)
            return
        for p in (10, 20, 30, 40):
            percent_list[index] = p
            backtrack(index + 1, l, percent_list)

    def calcul(percent_list):
        # 각각의 이모티콘에 퍼센트가 적용
        subs = 0
        ttotal = 0
        for user_percent, user_cost in users:
            # user_percent 이상일 경우 이모티콘 구매
            total = 0
            for p, e in zip(percent_list, emoticons):
                if p >= user_percent:
                    total += e - ((e // 10) * (p // 10))
            
            # 구매한 값이 user_cost를 넘을 경우 서비스 가입
            if total >= user_cost:
                subs += 1
            else:
                ttotal += total
                
        nonlocal answer
        if subs > answer[0]:
            answer[0], answer[1] = subs, ttotal
        elif subs == answer[0] and ttotal > answer[1]:
            answer[1] = ttotal
            
            
    backtrack(0, l, [0] * l)
        
    return answer