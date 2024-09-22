def solution(s):
    answer = []
    temp = s.replace('{', '').replace('}}', '').split("},")
    temp.sort(key=lambda x: len(x))
    visited = set()
    for elem in temp:
        for number in elem.split(','):
            number = int(number)
            if number not in visited:
                visited.add(number)
                answer.append(number)
            
    
    return answer