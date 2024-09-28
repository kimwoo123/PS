def solution(clothes):
    category = dict()
    len_ = dict()
    for cloth in clothes:
        name, cate = cloth
        if cate in category:
            category[cate].append(name)
            len_[cate] += 1
        else:
            category[cate] = [name]
            len_[cate] = 1
    
    answer = 1
    for v in len_.values():
        answer *= (v + 1)
        
    answer -=1
    return answer