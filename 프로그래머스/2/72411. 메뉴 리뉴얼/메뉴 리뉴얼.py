from itertools import combinations

def solution(orders, course):
    answer = []

    
    for length in course:
        count = dict()
        for order in orders:
            combo = combinations(sorted(order), length)
            for each in combo:
                c = ''.join(each)
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1
        
        max_count = -1
        for course_, count_ in sorted(count.items(), key=lambda x: -x[1]):
            if max_count <= count_ and count_ > 1:
                max_count = count_
                answer.append(course_)
            else:
                break
            
      
    answer.sort()
    return answer