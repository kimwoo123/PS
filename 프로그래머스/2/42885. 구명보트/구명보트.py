def solution(people, limit):
    people.sort()
    l = len(people)
    answer = l
    end_index = l - 1
    for i in range(l):
        while i < end_index: 
            if people[i] + people[end_index] <= limit:
                break
            end_index -= 1
        else:
            break
        end_index -= 1
        answer -= 1
    
    return answer